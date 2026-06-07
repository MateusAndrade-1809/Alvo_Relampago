import random

import pygame

from src.config import (
    ALTURA_TELA,
    AZUL,
    BRANCO,
    CINZA,
    FPS,
    LARGURA_TELA,
    MARGEM_ALVO,
    PONTOS_POR_ACERTO,
    PRETO,
    RAIO_ALVO,
    TITULO_JOGO,
    VERMELHO,
    VERMELHO_ESCURO,
    VIDAS_INICIAIS,
)
from src.funcoes import (
    calcular_pontos,
    clique_acertou_alvo,
    jogador_perdeu,
    tomar_dano,
)


def criar_alvo():
    """Cria um alvo em uma posicao aleatoria dentro da tela."""
    x = random.randint(MARGEM_ALVO, LARGURA_TELA - MARGEM_ALVO)
    y = random.randint(MARGEM_ALVO + 45, ALTURA_TELA - MARGEM_ALVO)

    return {
        "posicao": (x, y),
        "raio": RAIO_ALVO,
    }


def reiniciar_jogo():
    """Retorna o estado inicial da partida."""
    return {
        "pontuacao": 0,
        "vidas": VIDAS_INICIAIS,
        "alvo": criar_alvo(),
        "ativo": True,
    }


def desenhar_texto(tela, fonte, texto, cor, x, y):
    """Desenha um texto na tela."""
    imagem_texto = fonte.render(texto, True, cor)
    tela.blit(imagem_texto, (x, y))


def desenhar_alvo(tela, alvo):
    """Desenha o alvo clicavel."""
    pygame.draw.circle(tela, VERMELHO_ESCURO, alvo["posicao"], alvo["raio"] + 4)
    pygame.draw.circle(tela, VERMELHO, alvo["posicao"], alvo["raio"])
    pygame.draw.circle(tela, BRANCO, alvo["posicao"], alvo["raio"] // 2)
    pygame.draw.circle(tela, VERMELHO, alvo["posicao"], alvo["raio"] // 4)


def desenhar_jogo(tela, fonte, fonte_grande, estado):
    """Desenha todos os elementos principais do jogo."""
    tela.fill(CINZA)

    desenhar_texto(tela, fonte, f"Pontuacao: {estado['pontuacao']}", PRETO, 24, 18)
    desenhar_texto(tela, fonte, f"Vidas: {estado['vidas']}", PRETO, 650, 18)
    desenhar_alvo(tela, estado["alvo"])

    if not estado["ativo"]:
        desenhar_texto(tela, fonte_grande, "Fim de jogo", VERMELHO_ESCURO, 300, 245)
        desenhar_texto(tela, fonte, "Pressione ESPACO para reiniciar", AZUL, 255, 310)


def verificar_clique(estado, posicao_clique):
    """Atualiza pontos, vidas e posicao do alvo apos um clique."""
    if not estado["ativo"]:
        return estado

    alvo = estado["alvo"]
    acertou = clique_acertou_alvo(posicao_clique, alvo["posicao"], alvo["raio"])

    if acertou:
        estado["pontuacao"] = calcular_pontos(estado["pontuacao"], PONTOS_POR_ACERTO)
        estado["alvo"] = criar_alvo()
    else:
        estado["vidas"] = tomar_dano(estado["vidas"], 1)

    if jogador_perdeu(estado["vidas"]):
        estado["ativo"] = False

    return estado


def executar_jogo():
    """Executa a janela e o loop principal do Alvo Relampago."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    fonte = pygame.font.SysFont("arial", 28)
    fonte_grande = pygame.font.SysFont("arial", 48, bold=True)

    estado = reiniciar_jogo()
    rodando = True

    while rodando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False
                elif evento.key == pygame.K_SPACE and not estado["ativo"]:
                    estado = reiniciar_jogo()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                estado = verificar_clique(estado, evento.pos)

        desenhar_jogo(tela, fonte, fonte_grande, estado)
        pygame.display.flip()

    pygame.quit()
