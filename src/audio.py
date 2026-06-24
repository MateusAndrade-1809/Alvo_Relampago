import io
import math
import wave
from array import array

import pygame


def criar_som(frequencia, duracao, volume=0.25):
    """Cria um efeito sonoro simples sem depender de arquivo externo."""
    taxa_amostragem = 44100
    total_amostras = int(taxa_amostragem * duracao)
    amostras = array("h")

    for indice in range(total_amostras):
        tempo = indice / taxa_amostragem
        fade = 1 - indice / total_amostras
        valor = math.sin(2 * math.pi * frequencia * tempo)
        amostras.append(int(valor * volume * fade * 32767))

    memoria = io.BytesIO()
    with wave.open(memoria, "wb") as arquivo:
        arquivo.setnchannels(1)
        arquivo.setsampwidth(2)
        arquivo.setframerate(taxa_amostragem)
        arquivo.writeframes(amostras.tobytes())

    memoria.seek(0)
    return pygame.mixer.Sound(file=memoria)


class GerenciadorSons:
    """Carrega e toca os efeitos, mantendo o jogo funcional sem audio."""

    def __init__(self):
        self.disponivel = False
        self.sons = {}

        try:
            if pygame.mixer.get_init() is None:
                pygame.mixer.init(frequency=44100, size=-16, channels=1)

            self.sons = {
                "acerto": criar_som(880, 0.08),
                "erro": criar_som(180, 0.16),
                "item": criar_som(660, 0.14),
                "fim": criar_som(260, 0.28),
            }
            self.disponivel = True
        except pygame.error:
            self.disponivel = False

    def tocar(self, nome):
        if self.disponivel and nome in self.sons:
            self.sons[nome].play()

