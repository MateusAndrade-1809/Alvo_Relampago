import random

import pygame

from src.config import (
    ALTURA_TELA,
    AZUL,
    BRANCO,
    CAMINHO_RECORDE,
    CINZA,
    FPS,
    LARGURA_TELA,
    PONTOS_POR_ACERTO,
    PRETO,
    RAIO_ALVO,
    TEMPO_LIMITE,
    TITULO_JOGO,
    VERMELHO,
    VERMELHO_ESCURO,
    VIDAS_INICIAIS,
)
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


def criar_alvo():
    """Cria uma posicao aleatoria para o alvo."""
    alvo_x = random.randint(RAIO_ALVO, LARGURA_TELA - RAIO_ALVO)
    alvo_y = random.randint(90, ALTURA_TELA - RAIO_ALVO)

    return alvo_x, alvo_y


def desenhar_texto(tela, fonte, texto, cor, x, y):
    """Mostra um texto na tela."""
    imagem = fonte.render(texto, True, cor)
    tela.blit(imagem, (x, y))


def desenhar_alvo(tela, alvo_x, alvo_y):
    """Desenha o alvo vermelho."""
    pygame.draw.circle(tela, VERMELHO_ESCURO, (alvo_x, alvo_y), RAIO_ALVO + 4)
    pygame.draw.circle(tela, VERMELHO, (alvo_x, alvo_y), RAIO_ALVO)
    pygame.draw.circle(tela, BRANCO, (alvo_x, alvo_y), 20)
    pygame.draw.circle(tela, VERMELHO, (alvo_x, alvo_y), 9)


def desenhar_tela_inicial(tela, fonte_grande, fonte, botao_iniciar):
    """Desenha a tela inicial com o botao de iniciar."""
    desenhar_texto(tela, fonte_grande, "Alvo Relampago", VERMELHO_ESCURO, 235, 140)

    pygame.draw.rect(tela, AZUL, botao_iniciar)
    pygame.draw.rect(tela, PRETO, botao_iniciar, 3)
    desenhar_texto(tela, fonte, "Iniciar", BRANCO, 360, 268)

    desenhar_texto(tela, fonte, "Clique no alvo ate o tempo acabar.", PRETO, 205, 360)
    desenhar_texto(tela, fonte, "Tente conseguir o maximo de pontuacao possivel.", PRETO, 135, 400)


def desenhar_informacoes(tela, fonte, pontos, vidas, tempo_restante, recorde):
    """Desenha pontuacao, vidas, tempo, recorde e nivel."""
    nivel = calcular_nivel(pontos)

    desenhar_texto(tela, fonte, "Pontos: " + str(pontos), PRETO, 20, 20)
    desenhar_texto(tela, fonte, "Vidas: " + str(vidas), PRETO, 190, 20)
    desenhar_texto(tela, fonte, "Tempo: " + str(tempo_restante), PRETO, 330, 20)
    desenhar_texto(tela, fonte, "Recorde: " + str(recorde) + " pontos", PRETO, 500, 20)
    desenhar_texto(tela, fonte, "Nivel: " + nivel, AZUL, 20, 55)


def desenhar_tela_final(tela, fonte_grande, fonte, mensagem, pontos):
    """Mostra a tela final da partida."""
    nivel = calcular_nivel(pontos)

    desenhar_texto(tela, fonte_grande, mensagem, VERMELHO_ESCURO, 250, 235)
    desenhar_texto(tela, fonte, "Pontuacao final: " + str(pontos), PRETO, 285, 305)
    desenhar_texto(tela, fonte, "Nivel final: " + nivel, PRETO, 305, 345)
    desenhar_texto(tela, fonte, "Pressione ESPACO para jogar novamente", AZUL, 200, 390)
    desenhar_texto(tela, fonte, "Pressione ESC para sair", AZUL, 280, 430)


def reiniciar_partida():
    """Volta a partida para os valores iniciais."""
    pontos = 0
    vidas = VIDAS_INICIAIS
    alvo_x, alvo_y = criar_alvo()
    inicio = pygame.time.get_ticks()
    jogando = True
    mensagem = ""

    return pontos, vidas, alvo_x, alvo_y, inicio, jogando, mensagem


def verificar_fim_da_partida(pontos, vidas, tempo_restante):
    """Verifica se a partida acabou."""
    if jogador_perdeu(vidas):
        return False, "Fim de jogo"

    if tempo_acabou(tempo_restante):
        return False, "Tempo esgotado"

    return True, ""


def executar_jogo():
    """Executa o jogo Alvo Relampago."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    fonte = pygame.font.SysFont("arial", 28)
    fonte_grande = pygame.font.SysFont("arial", 48, bold=True)

    recorde = carregar_recorde(CAMINHO_RECORDE)
    pontos = 0
    vidas = VIDAS_INICIAIS
    alvo_x, alvo_y = criar_alvo()
    inicio = 0
    jogando = False
    mensagem = ""
    tempo_restante = TEMPO_LIMITE
    tela_inicial = True
    botao_iniciar = pygame.Rect(300, 250, 200, 70)
    rodando = True

    while rodando:
        relogio.tick(FPS)

        if jogando:
            segundos_passados = (pygame.time.get_ticks() - inicio) // 1000
            tempo_restante = calcular_tempo_restante(TEMPO_LIMITE, segundos_passados)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

                if evento.key == pygame.K_SPACE and tela_inicial:
                    pontos, vidas, alvo_x, alvo_y, inicio, jogando, mensagem = reiniciar_partida()
                    tela_inicial = False

                if evento.key == pygame.K_SPACE and not jogando and not tela_inicial:
                    pontos, vidas, alvo_x, alvo_y, inicio, jogando, mensagem = reiniciar_partida()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if tela_inicial and botao_iniciar.collidepoint(evento.pos):
                    pontos, vidas, alvo_x, alvo_y, inicio, jogando, mensagem = reiniciar_partida()
                    tela_inicial = False

                elif jogando:
                    acertou = clique_acertou_alvo(evento.pos, (alvo_x, alvo_y), RAIO_ALVO)

                    if acertou:
                        pontos = calcular_pontos(pontos, PONTOS_POR_ACERTO)
                        alvo_x, alvo_y = criar_alvo()
                    else:
                        vidas = tomar_dano(vidas, 1)

        if jogando:
            jogando, mensagem = verificar_fim_da_partida(pontos, vidas, tempo_restante)

            novo_recorde = atualizar_recorde(pontos, recorde)
            if novo_recorde != recorde:
                recorde = novo_recorde
                salvar_recorde(CAMINHO_RECORDE, recorde)

        tela.fill(CINZA)

        if tela_inicial:
            desenhar_tela_inicial(tela, fonte_grande, fonte, botao_iniciar)
        else:
            desenhar_informacoes(tela, fonte, pontos, vidas, tempo_restante, recorde)

            if jogando:
                desenhar_alvo(tela, alvo_x, alvo_y)
            else:
                desenhar_tela_final(tela, fonte_grande, fonte, mensagem, pontos)

        pygame.display.flip()

    pygame.quit()
