import ctypes
import sys

import pygame

from src.config import ALTURA_TELA, LARGURA_TELA


MODO_JANELA = "janela"
MODO_JANELA_CHEIA = "janela_cheia"
MODO_TELA_CHEIA = "tela_cheia"

MODOS_EXIBICAO = (MODO_JANELA, MODO_JANELA_CHEIA, MODO_TELA_CHEIA)

NOMES_MODOS = {
    MODO_JANELA: "Janela",
    MODO_JANELA_CHEIA: "Janela cheia",
    MODO_TELA_CHEIA: "Tela cheia",
}


def proximo_modo(modo_atual):
    """Alterna entre janela, janela maximizada e tela cheia."""
    indice = MODOS_EXIBICAO.index(modo_atual)
    return MODOS_EXIBICAO[(indice + 1) % len(MODOS_EXIBICAO)]


def calcular_area_exibicao(tamanho_janela):
    """Calcula a maior area 4:3 possivel, preservando a proporcao do jogo."""
    largura_janela, altura_janela = tamanho_janela
    escala = min(largura_janela / LARGURA_TELA, altura_janela / ALTURA_TELA)
    largura = max(1, round(LARGURA_TELA * escala))
    altura = max(1, round(ALTURA_TELA * escala))
    x = (largura_janela - largura) // 2
    y = (altura_janela - altura) // 2
    return pygame.Rect(x, y, largura, altura)


def converter_posicao_mouse(posicao, tamanho_janela):
    """Converte um clique da janela para as coordenadas logicas 800x600."""
    area = calcular_area_exibicao(tamanho_janela)
    if not area.collidepoint(posicao):
        return None

    x = int((posicao[0] - area.x) * LARGURA_TELA / area.width)
    y = int((posicao[1] - area.y) * ALTURA_TELA / area.height)
    return min(x, LARGURA_TELA - 1), min(y, ALTURA_TELA - 1)


def _maximizar_janela_windows():
    """Solicita ao Windows que maximize a janela criada pelo SDL."""
    if not sys.platform.startswith("win"):
        return False

    try:
        identificador = pygame.display.get_wm_info().get("window")
        if not identificador:
            return False
        ctypes.windll.user32.ShowWindow(identificador, 3)
        return True
    except (AttributeError, OSError):
        return False


def criar_janela(modo):
    """Cria a janela do Pygame no modo solicitado."""
    if modo == MODO_TELA_CHEIA:
        return pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    janela = pygame.display.set_mode(
        (LARGURA_TELA, ALTURA_TELA), pygame.RESIZABLE
    )

    if modo == MODO_JANELA_CHEIA and not _maximizar_janela_windows():
        tamanho_desktop = pygame.display.get_desktop_sizes()[0]
        janela = pygame.display.set_mode(tamanho_desktop, pygame.RESIZABLE)

    return janela


def apresentar_quadro(janela, quadro):
    """Apresenta o quadro logico com escala proporcional e barras pretas."""
    area = calcular_area_exibicao(janela.get_size())
    janela.fill((0, 0, 0))

    if area.size == quadro.get_size():
        imagem = quadro
    else:
        imagem = pygame.transform.smoothscale(quadro, area.size)

    janela.blit(imagem, area.topleft)
