import random

from src.config import (
    ALTURA_TELA,
    LARGURA_TELA,
    RAIO_ITEM,
    TAMANHOS_ALVO,
    VIDAS_MAXIMAS,
)


def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos com a pontuacao atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vidas, dano):
    """Tira vidas do jogador."""
    return vidas - dano


def curar_vida(vidas):
    """Adiciona 1 vida ao jogador, respeitando o limite maximo."""
    if vidas < VIDAS_MAXIMAS:
        return vidas + 1
    return vidas


def jogador_perdeu(vidas):
    """Verifica se o jogador perdeu todas as vidas."""
    return vidas <= 0


def atualizar_recorde(pontos, recorde):
    """Retorna o maior valor entre a pontuacao atual e o recorde."""
    if pontos > recorde:
        return pontos
    return recorde


def calcular_nivel(pontos):
    """Mostra o nivel do jogador de acordo com a pontuacao."""
    if pontos < 100:
        return "Iniciante"

    if pontos < 250:
        return "Intermediario"

    if pontos < 400:
        return "Excelente"

    if pontos < 600:
        return "Extraordinario"

    return "Deus"


def calcular_tempo_restante(tempo_limite, segundos_passados):
    """Calcula quanto tempo ainda falta para acabar a partida."""
    tempo_restante = tempo_limite - segundos_passados

    if tempo_restante < 0:
        return 0

    return tempo_restante


def tempo_acabou(tempo_restante):
    """Verifica se o tempo chegou a zero."""
    return tempo_restante <= 0


def clique_acertou_alvo(posicao_clique, posicao_alvo, raio_alvo):
    """Verifica se o clique do mouse acertou o alvo circular."""
    clique_x = posicao_clique[0]
    clique_y = posicao_clique[1]
    alvo_x = posicao_alvo[0]
    alvo_y = posicao_alvo[1]

    distancia_x = clique_x - alvo_x
    distancia_y = clique_y - alvo_y
    distancia = (distancia_x**2 + distancia_y**2) ** 0.5

    return distancia <= raio_alvo


def sortear_tamanho_alvo(pontos):
    """Retorna um tamanho de alvo aleatorio se o jogador tiver pontos suficientes."""
    from src.config import PONTUACAO_PARA_VARIAR_ALVO

    if pontos < PONTUACAO_PARA_VARIAR_ALVO:
        return "medio"

    return random.choice(["medio", "pequeno"])


def obter_raio_alvo(tamanho):
    """Retorna o raio correspondente ao tamanho do alvo."""
    return TAMANHOS_ALVO[tamanho]["raio"]


def obter_pontos_alvo(tamanho):
    """Retorna os pontos ganhos ao acertar um alvo do tamanho informado."""
    return TAMANHOS_ALVO[tamanho]["pontos"]


def criar_posicao_item():
    """Gera uma posicao aleatoria valida para um item especial."""
    x = random.randint(RAIO_ITEM + 10, LARGURA_TELA - RAIO_ITEM - 10)
    y = random.randint(90 + RAIO_ITEM, ALTURA_TELA - RAIO_ITEM - 10)
    return x, y


def item_foi_clicado(posicao_clique, posicao_item):
    """Verifica se o clique acertou um item especial (coracao ou ampulheta)."""
    return clique_acertou_alvo(posicao_clique, posicao_item, RAIO_ITEM)


def item_expirou(tempo_surgimento, tempo_atual, duracao):
    """Verifica se o item ficou tempo demais na tela sem ser coletado."""
    segundos_na_tela = (tempo_atual - tempo_surgimento) / 1000
    return segundos_na_tela >= duracao


def sortear_proximo_intervalo(intervalo_min, intervalo_max):
    """Sorteia um intervalo aleatorio (em segundos) para o proximo item aparecer."""
    return random.randint(intervalo_min, intervalo_max)
