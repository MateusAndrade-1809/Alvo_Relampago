from src.config import BONUS_TEMPO, RAIO_ITEM, TEMPO_LIMITE
from src.dados import (
    carregar_ranking,
    obter_jogadores_salvos,
    registrar_pontuacao,
    salvar_ranking,
)
from src.estado import Alvo, EstadoJogo, Estatisticas, ItemEspecial
from src.funcoes import (
    alvo_expirou,
    calcular_pontos_combo,
    calcular_tempo_restante,
    curar_vida,
    elementos_sobrepostos,
    item_expirou,
    obter_dificuldade,
    obter_pontos_alvo,
    obter_raio_alvo,
    posicao_esta_livre,
)
from src.jogo import (
    atualizar_alvo_expirado,
    atualizar_item,
    criar_alvo,
    processar_clique,
)


def test_curar_vida_respeita_limite_maximo():
    assert curar_vida(2) == 3
    assert curar_vida(3) == 3


def test_dificuldade_evolui_com_a_pontuacao():
    assert obter_dificuldade(0)["nome"] == "Aquecimento"
    assert obter_dificuldade(40)["nome"] == "Agil"
    assert obter_dificuldade(100)["nome"] == "Rapido"
    assert obter_dificuldade(250)["nome"] == "Relampago"


def test_elementos_sobrepostos_considera_raios_e_margem():
    assert elementos_sobrepostos((100, 100), 20, (130, 100), 20) is True
    assert elementos_sobrepostos((100, 100), 20, (160, 100), 20) is False


def test_alvo_novo_nao_sobrepoe_area_ocupada():
    ocupado = (400, 300, 120)

    for _ in range(30):
        alvo = criar_alvo(0, agora=100, ocupados=[ocupado])
        raio = obter_raio_alvo(alvo.tamanho)
        assert posicao_esta_livre(
            (alvo.x, alvo.y), raio, [ocupado]
        )


def test_item_novo_nao_sobrepoe_alvo():
    item = ItemEspecial(proximo_surgimento=0)
    alvo = (400, 300, 100)

    atualizar_item(item, agora=1000, ocupados=[alvo])

    assert item.ativo is True
    assert posicao_esta_livre((item.x, item.y), RAIO_ITEM, [alvo])


def test_itens_e_alvos_expiram_no_tempo_configurado():
    assert item_expirou(1000, 5999, 5) is False
    assert item_expirou(1000, 6000, 5) is True
    assert alvo_expirou(1000, 3999, 3) is False
    assert alvo_expirou(1000, 4000, 3) is True


def test_alvo_expirado_remove_vida_e_registra_estatistica():
    estado = EstadoJogo(combo=4)
    estado.alvo = Alvo(x=300, y=300, tamanho="medio", surgiu_em=0)

    expirou = atualizar_alvo_expirado(estado, agora=3000)

    assert expirou is True
    assert estado.vidas == 2
    assert estado.combo == 0
    assert estado.estatisticas.alvos_perdidos == 1


def test_combo_multiplica_pontos_e_erro_encerra_sequencia():
    estado = EstadoJogo()
    estado.alvo = Alvo(x=300, y=300, tamanho="medio", surgiu_em=0)
    pontos_esperados = 0

    for combo_esperado in range(1, 4):
        pontos_base = obter_pontos_alvo(estado.alvo.tamanho)
        pontos_esperados += calcular_pontos_combo(pontos_base, combo_esperado)
        resultado = processar_clique(
            estado, (estado.alvo.x, estado.alvo.y), agora=combo_esperado * 100
        )

        assert resultado == "acerto"
        assert estado.combo == combo_esperado

    assert estado.pontos == pontos_esperados
    assert estado.maior_combo == 3

    assert processar_clique(estado, (0, 0), agora=500) == "erro"
    assert estado.combo == 0
    assert estado.maior_combo == 3


def test_ampulheta_funciona_no_ultimo_segundo():
    estado = EstadoJogo(inicio=0)
    estado.alvo = Alvo(x=400, y=400, tamanho="medio")
    estado.ampulheta.ativar(100, 100, agora=25000)

    resultado = processar_clique(estado, (100, 100), agora=30000)
    segundos_passados = (30000 - estado.inicio) // 1000

    assert resultado == "item"
    assert estado.inicio == BONUS_TEMPO * 1000
    assert calcular_tempo_restante(TEMPO_LIMITE, segundos_passados) == BONUS_TEMPO


def test_estatisticas_calculam_precisao_e_tempo_jogado():
    estatisticas = Estatisticas(acertos=8, erros=2, coracoes=1, ampulhetas=1)
    estado = EstadoJogo(inicio_real=1000, fim=31500, estatisticas=estatisticas)

    assert estatisticas.precisao == 80
    assert estatisticas.total_cliques == 12
    assert estado.tempo_jogado == 30


def test_ranking_mantem_apenas_as_cinco_melhores_pontuacoes():
    ranking = [
        {"nome": "A", "pontos": 10},
        {"nome": "B", "pontos": 20},
        {"nome": "C", "pontos": 30},
        {"nome": "D", "pontos": 40},
        {"nome": "E", "pontos": 50},
    ]

    atualizado = registrar_pontuacao(ranking, "Novo", 35, limite=5)

    assert [resultado["pontos"] for resultado in atualizado] == [50, 40, 35, 30, 20]
    assert atualizado[2]["nome"] == "Novo"


def test_salvar_e_carregar_ranking(tmp_path):
    caminho = tmp_path / "ranking.txt"
    ranking = [
        {"nome": "Mateus", "pontos": 120},
        {"nome": "Daniel", "pontos": 90},
    ]

    salvar_ranking(caminho, ranking)

    assert carregar_ranking(caminho) == ranking


def test_ranking_ignora_linhas_invalidas_e_lista_nomes_unicos(tmp_path):
    caminho = tmp_path / "ranking.txt"
    caminho.write_text(
        "Mateus;120\nlinha quebrada\nMateus;80\nDaniel;nao-numero\nArthur;70\n",
        encoding="utf-8",
    )

    ranking = carregar_ranking(caminho)

    assert ranking == [
        {"nome": "Mateus", "pontos": 120},
        {"nome": "Mateus", "pontos": 80},
        {"nome": "Arthur", "pontos": 70},
    ]
    assert obter_jogadores_salvos(ranking) == ["Mateus", "Arthur"]
