from src.dados import carregar_recorde, salvar_recorde
from src.funcoes import (
    atualizar_recorde,
    calcular_nivel,
    calcular_pontos,
    calcular_tempo_restante,
    clique_acertou_alvo,
    jogador_perdeu,
    tempo_acabou,
    tomar_dano,
)


def test_calcular_pontos():
    assert calcular_pontos(10, 5) == 15


def test_tomar_dano():
    assert tomar_dano(3, 1) == 2


def test_jogador_perdeu():
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu():
    assert jogador_perdeu(2) is False


def test_atualizar_recorde_com_pontuacao_maior():
    assert atualizar_recorde(12, 8) == 12


def test_atualizar_recorde_com_pontuacao_menor():
    assert atualizar_recorde(4, 8) == 8


def test_calcular_tempo_restante():
    assert calcular_tempo_restante(30, 12) == 18


def test_calcular_tempo_restante_nao_fica_negativo():
    assert calcular_tempo_restante(30, 40) == 0


def test_tempo_acabou():
    assert tempo_acabou(0) is True


def test_tempo_nao_acabou():
    assert tempo_acabou(5) is False


def test_clique_acertou_alvo_no_centro():
    assert clique_acertou_alvo((100, 100), (100, 100), 35) is True


def test_clique_errou_alvo():
    assert clique_acertou_alvo((150, 100), (100, 100), 35) is False


def test_calcular_nivel_iniciante():
    assert calcular_nivel(0) == "Iniciante"


def test_calcular_nivel_intermediario():
    assert calcular_nivel(100) == "Intermediario"


def test_calcular_nivel_excelente():
    assert calcular_nivel(250) == "Excelente"


def test_calcular_nivel_extraordinario():
    assert calcular_nivel(400) == "Extraordinario"


def test_calcular_nivel_deus():
    assert calcular_nivel(600) == "Deus"


def test_salvar_e_carregar_recorde(tmp_path):
    arquivo = tmp_path / "recorde.txt"

    salvar_recorde(arquivo, 15)

    assert arquivo.read_text(encoding="utf-8") == "Recorde: 15 pontos"
    assert carregar_recorde(arquivo) == 15


def test_carregar_recorde_antigo_apenas_com_numero(tmp_path):
    arquivo = tmp_path / "recorde.txt"
    arquivo.write_text("20", encoding="utf-8")

    assert carregar_recorde(arquivo) == 20
