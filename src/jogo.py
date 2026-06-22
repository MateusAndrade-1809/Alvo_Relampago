import random
import math

import pygame

from src.config import (
    ALTURA_TELA,
    ALTURA_HUD,
    AMARELO,
    AZUL,
    BONUS_TEMPO,
    BRANCO,
    CAMINHO_RANKING,
    CAMINHO_RECORDE,
    CINZA,
    DURACAO_ITEM,
    FPS,
    INTERVALO_ITEM_MAX,
    INTERVALO_ITEM_MIN,
    LARANJA,
    LARGURA_TELA,
    LIMITE_NOME_JOGADOR,
    LIMITE_RANKING,
    MARGEM_ENTRE_ELEMENTOS,
    PRETO,
    RAIO_ITEM,
    ROSA,
    TEMPO_LIMITE,
    TITULO_JOGO,
    VERDE,
    VERMELHO,
    VERMELHO_ESCURO,
    VIDAS_INICIAIS,
)
from src.audio import GerenciadorSons
from src.dados import (
    carregar_ranking,
    carregar_recorde,
    obter_jogadores_salvos,
    registrar_pontuacao,
    salvar_ranking,
    salvar_recorde,
)
from src.estado import Alvo, EstadoJogo, Estatisticas, MensagemFlutuante
from src.exibicao import (
    MODO_JANELA,
    MODO_TELA_CHEIA,
    MODOS_EXIBICAO,
    NOMES_MODOS,
    apresentar_quadro,
    converter_posicao_mouse,
    criar_janela,
    proximo_modo,
)
from src.funcoes import (
    atualizar_combo,
    atualizar_recorde,
    alvo_expirou,
    calcular_multiplicador_combo,
    calcular_nivel,
    calcular_pontos,
    calcular_pontos_combo,
    calcular_tempo_restante,
    clique_acertou_alvo,
    criar_posicao_item,
    criar_posicao_livre,
    curar_vida,
    item_expirou,
    item_foi_clicado,
    jogador_perdeu,
    obter_pontos_alvo,
    obter_dificuldade,
    obter_raio_alvo,
    sortear_proximo_intervalo,
    sortear_tamanho_alvo,
    tempo_acabou,
    tomar_dano,
)


def criar_alvo(pontos, agora=0, ocupados=()):
    """Cria um alvo aleatorio dentro da area jogavel."""
    tamanho = sortear_tamanho_alvo(pontos)
    raio = obter_raio_alvo(tamanho)
    x, y = criar_posicao_livre(raio, ocupados)
    velocidade = obter_dificuldade(pontos)["velocidade"]

    if velocidade:
        angulo = random.uniform(0, math.tau)
        velocidade_x = math.cos(angulo) * velocidade
        velocidade_y = math.sin(angulo) * velocidade
    else:
        velocidade_x = 0
        velocidade_y = 0

    return Alvo(
        x=x,
        y=y,
        tamanho=tamanho,
        surgiu_em=agora,
        velocidade_x=velocidade_x,
        velocidade_y=velocidade_y,
    )


def desenhar_texto(tela, fonte, texto, cor, x, y):
    imagem = fonte.render(texto, True, cor)
    tela.blit(imagem, (x, y))


def desenhar_texto_centralizado(tela, fonte, texto, cor, y):
    imagem = fonte.render(texto, True, cor)
    x = (LARGURA_TELA - imagem.get_width()) // 2
    tela.blit(imagem, (x, y))


def desenhar_alvo(tela, alvo):
    raio = obter_raio_alvo(alvo.tamanho)
    centro = (round(alvo.x), round(alvo.y))
    pygame.draw.circle(tela, VERMELHO_ESCURO, centro, raio + 4)
    pygame.draw.circle(tela, VERMELHO, centro, raio)
    pygame.draw.circle(tela, BRANCO, centro, max(8, raio // 2))
    pygame.draw.circle(tela, VERMELHO, centro, max(4, raio // 4))


def desenhar_coracao(tela, x, y, raio=RAIO_ITEM):
    pygame.draw.circle(tela, ROSA, (x - raio // 2, y - raio // 4), raio // 2)
    pygame.draw.circle(tela, ROSA, (x + raio // 2, y - raio // 4), raio // 2)
    pontos = [(x - raio, y - raio // 4), (x, y + raio), (x + raio, y - raio // 4)]
    pygame.draw.polygon(tela, ROSA, pontos)


def desenhar_ampulheta(tela, x, y):
    raio = RAIO_ITEM
    topo = [(x - raio, y - raio), (x + raio, y - raio), (x, y)]
    base = [(x - raio, y + raio), (x + raio, y + raio), (x, y)]
    pygame.draw.polygon(tela, AMARELO, topo)
    pygame.draw.polygon(tela, AMARELO, base)
    pygame.draw.polygon(tela, LARANJA, topo, 2)
    pygame.draw.polygon(tela, LARANJA, base, 2)
    pygame.draw.line(tela, LARANJA, (x - raio, y - raio), (x + raio, y - raio), 3)
    pygame.draw.line(tela, LARANJA, (x - raio, y + raio), (x + raio, y + raio), 3)


def criar_botoes_jogadores(ranking):
    """Cria botoes para selecionar nomes que ja aparecem no ranking."""
    botoes = []
    nomes = obter_jogadores_salvos(ranking)
    largura = 130
    espacamento = 10
    largura_total = len(nomes) * largura + max(0, len(nomes) - 1) * espacamento
    inicio_x = (LARGURA_TELA - largura_total) // 2

    for indice, nome in enumerate(nomes):
        retangulo = pygame.Rect(
            inicio_x + indice * (largura + espacamento), 455, largura, 38
        )
        botoes.append((retangulo, nome))

    return botoes


def criar_botoes_modos():
    """Cria os tres botoes de modo de exibicao da tela inicial."""
    largura = 145
    altura = 34
    espacamento = 10
    largura_total = len(MODOS_EXIBICAO) * largura + (
        len(MODOS_EXIBICAO) - 1
    ) * espacamento
    inicio_x = (LARGURA_TELA - largura_total) // 2

    return [
        (
            pygame.Rect(
                inicio_x + indice * (largura + espacamento),
                18,
                largura,
                altura,
            ),
            modo,
        )
        for indice, modo in enumerate(MODOS_EXIBICAO)
    ]


def desenhar_tela_inicial(
    tela,
    fonte_grande,
    fonte,
    fonte_pequena,
    botao_iniciar,
    campo_nome,
    nome_jogador,
    botoes_jogadores,
    botoes_modos,
    modo_exibicao,
):
    for retangulo, modo in botoes_modos:
        selecionado = modo == modo_exibicao
        cor_fundo = AZUL if selecionado else BRANCO
        cor_texto = BRANCO if selecionado else PRETO
        pygame.draw.rect(tela, cor_fundo, retangulo, border_radius=6)
        pygame.draw.rect(tela, AZUL, retangulo, 2, border_radius=6)
        imagem = fonte_pequena.render(NOMES_MODOS[modo], True, cor_texto)
        tela.blit(imagem, imagem.get_rect(center=retangulo.center))

    desenhar_texto_centralizado(
        tela, fonte_grande, "Alvo Relampago", VERMELHO_ESCURO, 80
    )
    desenhar_texto_centralizado(tela, fonte, "Digite seu nome:", PRETO, 155)
    pygame.draw.rect(tela, BRANCO, campo_nome, border_radius=6)
    pygame.draw.rect(tela, AZUL, campo_nome, 3, border_radius=6)
    texto_nome = nome_jogador or "Novo jogador"
    cor_nome = PRETO if nome_jogador else (120, 120, 120)
    desenhar_texto(
        tela, fonte, texto_nome, cor_nome, campo_nome.x + 12, campo_nome.y + 9
    )

    pygame.draw.rect(tela, AZUL, botao_iniciar, border_radius=8)
    pygame.draw.rect(tela, PRETO, botao_iniciar, 3, border_radius=8)
    desenhar_texto_centralizado(tela, fonte, "Iniciar", BRANCO, 278)
    desenhar_texto_centralizado(
        tela, fonte_pequena, "Clique nos alvos antes que desaparecam.", PRETO, 355
    )
    desenhar_texto_centralizado(
        tela, fonte_pequena, "Clique fora do alvo e voce perde uma vida.", PRETO, 382
    )

    if botoes_jogadores:
        desenhar_texto_centralizado(
            tela, fonte_pequena, "Ou selecione um jogador salvo:", AZUL, 420
        )
        for retangulo, nome in botoes_jogadores:
            pygame.draw.rect(tela, BRANCO, retangulo, border_radius=6)
            pygame.draw.rect(tela, AZUL, retangulo, 2, border_radius=6)
            imagem = fonte_pequena.render(nome[:12], True, PRETO)
            tela.blit(imagem, imagem.get_rect(center=retangulo.center))

    desenhar_coracao(tela, 190, 535, raio=14)
    desenhar_texto(tela, fonte_pequena, "recupera 1 vida", PRETO, 215, 523)
    desenhar_ampulheta(tela, 495, 535)
    desenhar_texto(tela, fonte_pequena, "adiciona 5 segundos", PRETO, 525, 523)


def desenhar_vidas(tela, vidas, x, y):
    for indice in range(vidas):
        desenhar_coracao(tela, x + indice * 28, y, raio=8)


def desenhar_informacoes(tela, fonte, fonte_tempo, estado, recorde):
    nivel = calcular_nivel(estado.pontos)
    fase = obter_dificuldade(estado.pontos)["nome"]
    desenhar_texto(tela, fonte, f"Pontos: {estado.pontos}", PRETO, 20, 20)
    desenhar_texto(tela, fonte, "Vidas:", PRETO, 190, 20)
    desenhar_vidas(tela, estado.vidas, 265, 32)
    cor_tempo = VERMELHO if estado.tempo_restante <= 5 else PRETO
    desenhar_texto(
        tela,
        fonte_tempo if estado.tempo_restante <= 5 else fonte,
        f"Tempo: {estado.tempo_restante}",
        cor_tempo,
        330,
        16 if estado.tempo_restante <= 5 else 20,
    )
    desenhar_texto(tela, fonte, f"Recorde: {recorde} pts", PRETO, 500, 20)
    desenhar_texto(tela, fonte, f"Nivel: {nivel} | Fase: {fase}", AZUL, 20, 55)
    multiplicador = calcular_multiplicador_combo(estado.combo)
    desenhar_texto(
        tela,
        fonte,
        f"Combo: {estado.combo} (x{multiplicador})",
        LARANJA,
        535,
        55,
    )


def desenhar_ranking(tela, fonte_pequena, ranking, y_inicial):
    desenhar_texto_centralizado(tela, fonte_pequena, "TOP 5", AZUL, y_inicial)
    for indice, resultado in enumerate(ranking, start=1):
        texto = f"{indice}. {resultado['nome']} - {resultado['pontos']} pts"
        desenhar_texto_centralizado(
            tela, fonte_pequena, texto, PRETO, y_inicial + indice * 28
        )


def desenhar_tela_final(tela, fonte_grande, fonte, fonte_pequena, estado, ranking):
    desenhar_texto_centralizado(
        tela, fonte_grande, estado.mensagem, VERMELHO_ESCURO, 80
    )
    desenhar_texto_centralizado(
        tela, fonte, estado.nome_jogador, AZUL, 140
    )
    desenhar_texto_centralizado(
        tela, fonte, f"Pontuacao final: {estado.pontos}", PRETO, 180
    )
    desenhar_texto_centralizado(
        tela,
        fonte_pequena,
        (
            f"Acertos: {estado.estatisticas.acertos} | "
            f"Erros: {estado.estatisticas.erros} | "
            f"Alvos perdidos: {estado.estatisticas.alvos_perdidos}"
        ),
        PRETO,
        225,
    )
    desenhar_texto_centralizado(
        tela,
        fonte_pequena,
        (
            f"Precisao: {estado.estatisticas.precisao}% | "
            f"Itens: {estado.estatisticas.coracoes + estado.estatisticas.ampulhetas} | "
            f"Tempo jogado: {estado.tempo_jogado}s"
        ),
        PRETO,
        252,
    )
    desenhar_texto_centralizado(
        tela,
        fonte_pequena,
        (
            f"Nivel final: {calcular_nivel(estado.pontos)} | "
            f"Maior combo: {estado.maior_combo}"
        ),
        AZUL,
        279,
    )
    desenhar_ranking(tela, fonte_pequena, ranking, 315)
    desenhar_texto_centralizado(
        tela, fonte_pequena, "ESPACO: jogar novamente | ESC: sair", AZUL, 525
    )


def reiniciar_partida(estado, agora):
    estado.pontos = 0
    estado.combo = 0
    estado.maior_combo = 0
    estado.vidas = VIDAS_INICIAIS
    estado.tempo_restante = TEMPO_LIMITE
    estado.inicio = agora
    estado.inicio_real = agora
    estado.fim = 0
    estado.ultimo_frame = agora
    estado.tela = "jogo"
    estado.mensagem = ""
    estado.resultado_salvo = False
    estado.alvo = criar_alvo(estado.pontos, agora)
    estado.coracao.desativar()
    estado.ampulheta.desativar()
    estado.coracao.proximo_surgimento = agora + (
        sortear_proximo_intervalo(INTERVALO_ITEM_MIN, INTERVALO_ITEM_MAX) * 1000
    )
    estado.ampulheta.proximo_surgimento = agora + (
        sortear_proximo_intervalo(INTERVALO_ITEM_MIN, INTERVALO_ITEM_MAX) * 1000
    )
    estado.estatisticas = Estatisticas()
    estado.mensagens.clear()
    estado.flash_ate = 0


def verificar_fim_da_partida(vidas, tempo_restante):
    if jogador_perdeu(vidas):
        return "Fim de jogo"
    if tempo_acabou(tempo_restante):
        return "Tempo esgotado"
    return ""


def obter_circulos_ocupados(estado, ignorar=None):
    """Monta a lista de circulos visiveis para evitar sobreposicoes."""
    ocupados = []
    if ignorar != "alvo":
        ocupados.append(
            (estado.alvo.x, estado.alvo.y, obter_raio_alvo(estado.alvo.tamanho))
        )
    if estado.coracao.ativo and ignorar != "coracao":
        ocupados.append((estado.coracao.x, estado.coracao.y, RAIO_ITEM))
    if estado.ampulheta.ativo and ignorar != "ampulheta":
        ocupados.append((estado.ampulheta.x, estado.ampulheta.y, RAIO_ITEM))
    return ocupados


def atualizar_item(item, agora, ocupados):
    if not item.ativo and agora >= item.proximo_surgimento:
        x, y = criar_posicao_item(ocupados)
        item.ativar(x, y, agora)
    elif item.ativo and item_expirou(item.surgiu_em, agora, DURACAO_ITEM):
        item.desativar()
        item.proximo_surgimento = agora + (
            sortear_proximo_intervalo(INTERVALO_ITEM_MIN, INTERVALO_ITEM_MAX) * 1000
        )


def agendar_proximo_item(item, agora):
    item.desativar()
    item.proximo_surgimento = agora + (
        sortear_proximo_intervalo(INTERVALO_ITEM_MIN, INTERVALO_ITEM_MAX) * 1000
    )


def criar_novo_alvo(estado, agora):
    estado.alvo = criar_alvo(
        estado.pontos,
        agora,
        obter_circulos_ocupados(estado, ignorar="alvo"),
    )


def adicionar_feedback(estado, texto, x, y, cor, agora):
    estado.mensagens.append(
        MensagemFlutuante(
            texto=texto,
            x=round(x),
            y=round(y),
            cor=cor,
            criada_em=agora,
        )
    )


def atualizar_feedbacks(estado, agora):
    estado.mensagens = [
        mensagem
        for mensagem in estado.mensagens
        if agora - mensagem.criada_em < mensagem.duracao
    ]


def desenhar_feedbacks(tela, fonte_pequena, estado, agora):
    for mensagem in estado.mensagens:
        progresso = (agora - mensagem.criada_em) / mensagem.duracao
        imagem = fonte_pequena.render(mensagem.texto, True, mensagem.cor)
        imagem.set_alpha(max(0, round(255 * (1 - progresso))))
        x = mensagem.x - imagem.get_width() // 2
        y = mensagem.y - round(progresso * 35)
        tela.blit(imagem, (x, y))


def desenhar_flash_dano(tela, estado, agora):
    if agora >= estado.flash_ate:
        return

    camada = pygame.Surface((LARGURA_TELA, ALTURA_TELA), pygame.SRCALPHA)
    camada.fill((220, 45, 45, 55))
    tela.blit(camada, (0, 0))


def atualizar_movimento_alvo(estado, delta_segundos):
    alvo = estado.alvo
    if alvo.velocidade_x == 0 and alvo.velocidade_y == 0:
        return

    raio = obter_raio_alvo(alvo.tamanho)
    novo_x = alvo.x + alvo.velocidade_x * delta_segundos
    novo_y = alvo.y + alvo.velocidade_y * delta_segundos

    if novo_x - raio < 10 or novo_x + raio > LARGURA_TELA - 10:
        alvo.velocidade_x *= -1
        novo_x = alvo.x + alvo.velocidade_x * delta_segundos

    if novo_y - raio < ALTURA_HUD or novo_y + raio > ALTURA_TELA - 10:
        alvo.velocidade_y *= -1
        novo_y = alvo.y + alvo.velocidade_y * delta_segundos

    itens = obter_circulos_ocupados(estado, ignorar="alvo")
    sobrepoe_item = any(
        (novo_x - x) ** 2 + (novo_y - y) ** 2
        < (raio + outro_raio + MARGEM_ENTRE_ELEMENTOS) ** 2
        for x, y, outro_raio in itens
    )
    if sobrepoe_item:
        alvo.velocidade_x *= -1
        alvo.velocidade_y *= -1
        return

    alvo.x = novo_x
    alvo.y = novo_y


def atualizar_alvo_expirado(estado, agora):
    duracao = obter_dificuldade(estado.pontos)["duracao_alvo"]
    if alvo_expirou(estado.alvo.surgiu_em, agora, duracao):
        estado.combo = atualizar_combo(estado.combo, False)
        estado.vidas = tomar_dano(estado.vidas, 1)
        estado.estatisticas.alvos_perdidos += 1
        estado.flash_ate = agora + 180
        adicionar_feedback(
            estado,
            "Alvo perdido: -1 vida",
            estado.alvo.x,
            estado.alvo.y,
            VERMELHO,
            agora,
        )
        criar_novo_alvo(estado, agora)
        return True
    return False


def processar_clique(estado, posicao, agora):
    raio_alvo = obter_raio_alvo(estado.alvo.tamanho)

    if estado.coracao.ativo and item_foi_clicado(
        posicao, (estado.coracao.x, estado.coracao.y)
    ):
        vidas_anteriores = estado.vidas
        estado.vidas = curar_vida(estado.vidas)
        estado.estatisticas.coracoes += 1
        texto = "+1 vida" if estado.vidas > vidas_anteriores else "Vida cheia"
        adicionar_feedback(
            estado, texto, estado.coracao.x, estado.coracao.y, VERDE, agora
        )
        agendar_proximo_item(estado.coracao, agora)
        return "item"
    elif estado.ampulheta.ativo and item_foi_clicado(
        posicao, (estado.ampulheta.x, estado.ampulheta.y)
    ):
        estado.inicio += BONUS_TEMPO * 1000
        estado.estatisticas.ampulhetas += 1
        adicionar_feedback(
            estado,
            f"+{BONUS_TEMPO} segundos",
            estado.ampulheta.x,
            estado.ampulheta.y,
            AMARELO,
            agora,
        )
        agendar_proximo_item(estado.ampulheta, agora)
        return "item"
    elif clique_acertou_alvo(
        posicao, (estado.alvo.x, estado.alvo.y), raio_alvo
    ):
        estado.combo = atualizar_combo(estado.combo, True)
        estado.maior_combo = max(estado.maior_combo, estado.combo)
        pontos_base = obter_pontos_alvo(estado.alvo.tamanho)
        pontos_ganhos = calcular_pontos_combo(pontos_base, estado.combo)
        multiplicador = calcular_multiplicador_combo(estado.combo)
        estado.pontos = calcular_pontos(estado.pontos, pontos_ganhos)
        estado.estatisticas.acertos += 1
        adicionar_feedback(
            estado,
            f"+{pontos_ganhos} (x{multiplicador})",
            estado.alvo.x,
            estado.alvo.y,
            VERDE,
            agora,
        )
        criar_novo_alvo(estado, agora)
        return "acerto"
    else:
        estado.combo = atualizar_combo(estado.combo, False)
        estado.vidas = tomar_dano(estado.vidas, 1)
        estado.estatisticas.erros += 1
        estado.flash_ate = agora + 180
        adicionar_feedback(
            estado, "-1 vida", posicao[0], posicao[1], VERMELHO, agora
        )
        return "erro"


def executar_jogo():
    pygame.init()
    modo_exibicao = MODO_JANELA
    modo_antes_tela_cheia = MODO_JANELA
    janela = criar_janela(modo_exibicao)
    tela = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()
    fonte = pygame.font.SysFont("arial", 28)
    fonte_grande = pygame.font.SysFont("arial", 48, bold=True)
    fonte_pequena = pygame.font.SysFont("arial", 20)
    fonte_tempo = pygame.font.SysFont("arial", 32, bold=True)
    sons = GerenciadorSons()

    recorde = carregar_recorde(CAMINHO_RECORDE)
    ranking = carregar_ranking(CAMINHO_RANKING)[:LIMITE_RANKING]
    estado = EstadoJogo()
    estado.alvo = criar_alvo(0)
    botao_iniciar = pygame.Rect(300, 260, 200, 70)
    campo_nome = pygame.Rect(250, 195, 300, 52)
    rodando = True

    while rodando:
        relogio.tick(FPS)
        agora = pygame.time.get_ticks()

        if estado.tela == "jogo":
            delta_segundos = max(0, agora - estado.ultimo_frame) / 1000
            estado.ultimo_frame = agora
            segundos_passados = (agora - estado.inicio) // 1000
            estado.tempo_restante = calcular_tempo_restante(
                TEMPO_LIMITE, segundos_passados
            )
            atualizar_movimento_alvo(estado, delta_segundos)
            if atualizar_alvo_expirado(estado, agora):
                sons.tocar("erro")
            atualizar_item(
                estado.coracao,
                agora,
                obter_circulos_ocupados(estado, ignorar="coracao"),
            )
            atualizar_item(
                estado.ampulheta,
                agora,
                obter_circulos_ocupados(estado, ignorar="ampulheta"),
            )

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_F11:
                    modo_exibicao = proximo_modo(modo_exibicao)
                    if modo_exibicao != MODO_TELA_CHEIA:
                        modo_antes_tela_cheia = modo_exibicao
                    janela = criar_janela(modo_exibicao)
                elif evento.key == pygame.K_RETURN and (
                    evento.mod & pygame.KMOD_ALT
                ):
                    if modo_exibicao == MODO_TELA_CHEIA:
                        modo_exibicao = modo_antes_tela_cheia
                    else:
                        modo_antes_tela_cheia = modo_exibicao
                        modo_exibicao = MODO_TELA_CHEIA
                    janela = criar_janela(modo_exibicao)
                elif evento.key == pygame.K_ESCAPE:
                    rodando = False
                elif estado.tela == "inicio":
                    if evento.key == pygame.K_RETURN:
                        estado.nome_jogador = estado.nome_jogador.strip() or "Jogador"
                        reiniciar_partida(estado, agora)
                    elif evento.key == pygame.K_BACKSPACE:
                        estado.nome_jogador = estado.nome_jogador[:-1]
                    elif (
                        evento.unicode.isprintable()
                        and len(estado.nome_jogador) < LIMITE_NOME_JOGADOR
                    ):
                        estado.nome_jogador += evento.unicode
                elif evento.key == pygame.K_SPACE and estado.tela != "jogo":
                    reiniciar_partida(estado, agora)
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                posicao = converter_posicao_mouse(evento.pos, janela.get_size())
                if posicao is None:
                    continue

                if estado.tela == "inicio":
                    modo_selecionado = next(
                        (
                            modo
                            for retangulo, modo in criar_botoes_modos()
                            if retangulo.collidepoint(posicao)
                        ),
                        None,
                    )
                    if modo_selecionado is not None:
                        modo_exibicao = modo_selecionado
                        if modo_exibicao != MODO_TELA_CHEIA:
                            modo_antes_tela_cheia = modo_exibicao
                        janela = criar_janela(modo_exibicao)
                        continue

                if estado.tela == "inicio" and botao_iniciar.collidepoint(posicao):
                    estado.nome_jogador = estado.nome_jogador.strip() or "Jogador"
                    reiniciar_partida(estado, agora)
                elif estado.tela == "inicio":
                    for retangulo, nome in criar_botoes_jogadores(ranking):
                        if retangulo.collidepoint(posicao):
                            estado.nome_jogador = nome
                            break
                elif estado.tela == "jogo" and estado.vidas > 0:
                    resultado_clique = processar_clique(estado, posicao, agora)
                    sons.tocar(resultado_clique)

        if estado.tela == "jogo":
            # Recalcula depois dos eventos para que uma ampulheta coletada no
            # ultimo instante realmente evite o encerramento da partida.
            segundos_passados = (agora - estado.inicio) // 1000
            estado.tempo_restante = calcular_tempo_restante(
                TEMPO_LIMITE, segundos_passados
            )
            mensagem_fim = verificar_fim_da_partida(
                estado.vidas, estado.tempo_restante
            )
            if mensagem_fim:
                estado.tela = "fim"
                estado.mensagem = mensagem_fim
                estado.fim = agora

            if estado.tela == "fim" and not estado.resultado_salvo:
                ranking = registrar_pontuacao(
                    ranking,
                    estado.nome_jogador,
                    estado.pontos,
                    LIMITE_RANKING,
                )
                salvar_ranking(CAMINHO_RANKING, ranking)
                estado.resultado_salvo = True
                sons.tocar("fim")

            novo_recorde = atualizar_recorde(estado.pontos, recorde)
            if novo_recorde != recorde:
                recorde = novo_recorde
                salvar_recorde(CAMINHO_RECORDE, recorde)

        tela.fill(CINZA)
        atualizar_feedbacks(estado, agora)
        if estado.tela == "inicio":
            botoes_jogadores = criar_botoes_jogadores(ranking)
            botoes_modos = criar_botoes_modos()
            desenhar_tela_inicial(
                tela,
                fonte_grande,
                fonte,
                fonte_pequena,
                botao_iniciar,
                campo_nome,
                estado.nome_jogador,
                botoes_jogadores,
                botoes_modos,
                modo_exibicao,
            )
        else:
            desenhar_informacoes(tela, fonte, fonte_tempo, estado, recorde)
            if estado.tela == "jogo":
                desenhar_alvo(tela, estado.alvo)
                if estado.coracao.ativo:
                    desenhar_coracao(tela, estado.coracao.x, estado.coracao.y)
                if estado.ampulheta.ativo:
                    desenhar_ampulheta(tela, estado.ampulheta.x, estado.ampulheta.y)
                desenhar_feedbacks(tela, fonte_pequena, estado, agora)
                desenhar_flash_dano(tela, estado, agora)
            else:
                desenhar_tela_final(
                    tela, fonte_grande, fonte, fonte_pequena, estado, ranking
                )

        apresentar_quadro(janela, tela)
        pygame.display.flip()

    pygame.quit()
