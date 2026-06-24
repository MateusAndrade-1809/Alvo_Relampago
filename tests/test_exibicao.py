import pygame

from src.exibicao import (
    MODO_JANELA,
    MODO_JANELA_CHEIA,
    MODO_TELA_CHEIA,
    calcular_area_exibicao,
    converter_posicao_mouse,
    proximo_modo,
)


def test_proximo_modo_percorre_as_tres_opcoes():
    assert proximo_modo(MODO_JANELA) == MODO_JANELA_CHEIA
    assert proximo_modo(MODO_JANELA_CHEIA) == MODO_TELA_CHEIA
    assert proximo_modo(MODO_TELA_CHEIA) == MODO_JANELA


def test_area_exibicao_preserva_proporcao_em_tela_16_por_9():
    area = calcular_area_exibicao((1366, 768))

    assert area.size == (1024, 768)
    assert area.x == 171
    assert area.y == 0


def test_converter_mouse_remove_barras_laterais():
    tamanho_janela = (1366, 768)

    assert converter_posicao_mouse((683, 384), tamanho_janela) == (400, 300)
    assert converter_posicao_mouse((50, 300), tamanho_janela) is None


def test_converter_mouse_em_janela_original_nao_altera_posicao():
    assert converter_posicao_mouse((250, 400), (800, 600)) == (250, 400)


def test_area_exibicao_cabe_em_janela_vertical():
    area = calcular_area_exibicao((600, 800))

    assert area.size == (600, 450)
    assert area.x == 0
    assert area.y == 175
    assert isinstance(area, pygame.Rect)
