import random

from src.config import (
    ALTURA_TELA,
    ALTURA_HUD,
    FASES_DIFICULDADE,
    LARGURA_TELA,
    MARGEM_ENTRE_ELEMENTOS,
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


def obter_dificuldade(pontos):
    """Retorna a fase de dificuldade correspondente a pontuacao."""
    dificuldade_atual = FASES_DIFICULDADE[0]

    for dificuldade in FASES_DIFICULDADE:
        if pontos >= dificuldade["pontos_minimos"]:
            dificuldade_atual = dificuldade
        else:
            break

    return dificuldade_atual


def sortear_tamanho_alvo(pontos):
    """Sorteia um tamanho permitido pela dificuldade atual."""
    dificuldade = obter_dificuldade(pontos)
    return random.choice(dificuldade["tamanhos"])


def obter_raio_alvo(tamanho):
    """Retorna o raio correspondente ao tamanho do alvo."""
    return TAMANHOS_ALVO[tamanho]["raio"]


def obter_pontos_alvo(tamanho):
    """Retorna os pontos ganhos ao acertar um alvo do tamanho informado."""
    return TAMANHOS_ALVO[tamanho]["pontos"]


def elementos_sobrepostos(posicao_a, raio_a, posicao_b, raio_b, margem=0):
    """Verifica se dois elementos circulares ocupam a mesma area."""
    distancia_x = posicao_a[0] - posicao_b[0]
    distancia_y = posicao_a[1] - posicao_b[1]
    distancia_quadrada = distancia_x**2 + distancia_y**2
    distancia_minima = raio_a + raio_b + margem
    return distancia_quadrada < distancia_minima**2


def posicao_esta_livre(posicao, raio, ocupados, margem=MARGEM_ENTRE_ELEMENTOS):
    """Verifica se uma posicao nao invade nenhum circulo ocupado."""
    return all(
        not elementos_sobrepostos(posicao, raio, (x, y), outro_raio, margem)
        for x, y, outro_raio in ocupados
    )


def criar_posicao_livre(raio, ocupados=()):
    """Gera uma posicao valida sem sobrepor alvo ou itens existentes."""
    x_minimo = raio + 10
    x_maximo = LARGURA_TELA - raio - 10
    y_minimo = ALTURA_HUD + raio
    y_maximo = ALTURA_TELA - raio - 10

    for _ in range(100):
        posicao = (
            random.randint(x_minimo, x_maximo),
            random.randint(y_minimo, y_maximo),
        )
        if posicao_esta_livre(posicao, raio, ocupados):
            return posicao

    # A busca em grade garante uma alternativa mesmo com uma sequencia
    # aleatoria desfavoravel.
    passo = max(raio * 2, 20)
    for y in range(y_minimo, y_maximo + 1, passo):
        for x in range(x_minimo, x_maximo + 1, passo):
            if posicao_esta_livre((x, y), raio, ocupados):
                return x, y

    return LARGURA_TELA // 2, (ALTURA_HUD + ALTURA_TELA) // 2


def criar_posicao_item(ocupados=()):
    """Gera uma posicao aleatoria valida para um item especial."""
    return criar_posicao_livre(RAIO_ITEM, ocupados)


def item_foi_clicado(posicao_clique, posicao_item):
    """Verifica se o clique acertou um item especial (coracao ou ampulheta)."""
    return clique_acertou_alvo(posicao_clique, posicao_item, RAIO_ITEM)


def item_expirou(tempo_surgimento, tempo_atual, duracao):
    """Verifica se o item ficou tempo demais na tela sem ser coletado."""
    segundos_na_tela = (tempo_atual - tempo_surgimento) / 1000
    return segundos_na_tela >= duracao


def alvo_expirou(tempo_surgimento, tempo_atual, duracao):
    """Verifica se o jogador demorou demais para acertar o alvo."""
    segundos_na_tela = (tempo_atual - tempo_surgimento) / 1000
    return segundos_na_tela >= duracao


def sortear_proximo_intervalo(intervalo_min, intervalo_max):
    """Sorteia um intervalo aleatorio (em segundos) para o proximo item aparecer."""
    return random.randint(intervalo_min, intervalo_max)
