import random

import pygame

from src.config import (
    ALTURA_TELA,
    AMARELO,
    AZUL,
    BONUS_TEMPO,
    BRANCO,
    CAMINHO_RECORDE,
    CINZA,
    DURACAO_ITEM,
    FPS,
    INTERVALO_ITEM_MAX,
    INTERVALO_ITEM_MIN,
    LARANJA,
    LARGURA_TELA,
    PONTOS_POR_ACERTO,
    PRETO,
    RAIO_ALVO,
    RAIO_ITEM,
    ROSA,
    TEMPO_LIMITE,
    TITULO_JOGO,
    VERDE,
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
    criar_posicao_item,
    curar_vida,
    item_expirou,
    item_foi_clicado,
    jogador_perdeu,
    obter_pontos_alvo,
    obter_raio_alvo,
    sortear_proximo_intervalo,
    sortear_tamanho_alvo,
    tempo_acabou,
    tomar_dano,
)


# ---------------------------------------------------------------------------
# Criacao de elementos
# ---------------------------------------------------------------------------

def criar_alvo(pontos):
    """Cria uma posicao e tamanho aleatorio para o alvo."""
    tamanho = sortear_tamanho_alvo(pontos)
    raio = obter_raio_alvo(tamanho)

    alvo_x = random.randint(raio, LARGURA_TELA - raio)
    alvo_y = random.randint(90 + raio, ALTURA_TELA - raio)

    return alvo_x, alvo_y, tamanho


# ---------------------------------------------------------------------------
# Desenho na tela
# ---------------------------------------------------------------------------

def desenhar_texto(tela, fonte, texto, cor, x, y):
    """Mostra um texto na tela."""
    imagem = fonte.render(texto, True, cor)
    tela.blit(imagem, (x, y))


def desenhar_alvo(tela, alvo_x, alvo_y, raio):
    """Desenha o alvo vermelho com o tamanho informado."""
    pygame.draw.circle(tela, VERMELHO_ESCURO, (alvo_x, alvo_y), raio + 4)
    pygame.draw.circle(tela, VERMELHO, (alvo_x, alvo_y), raio)
    centro_branco = max(8, raio // 2)
    centro_vermelho = max(4, raio // 4)
    pygame.draw.circle(tela, BRANCO, (alvo_x, alvo_y), centro_branco)
    pygame.draw.circle(tela, VERMELHO, (alvo_x, alvo_y), centro_vermelho)


def desenhar_coracao(tela, x, y):
    """Desenha um coracao rosa na posicao informada."""
    raio = RAIO_ITEM
    pygame.draw.circle(tela, ROSA, (x - raio // 2, y - raio // 4), raio // 2)
    pygame.draw.circle(tela, ROSA, (x + raio // 2, y - raio // 4), raio // 2)
    pontos = [
        (x - raio, y - raio // 4),
        (x, y + raio),
        (x + raio, y - raio // 4),
    ]
    pygame.draw.polygon(tela, ROSA, pontos)


def desenhar_ampulheta(tela, x, y):
    """Desenha uma ampulheta amarela na posicao informada."""
    r = RAIO_ITEM
    topo = [
        (x - r, y - r),
        (x + r, y - r),
        (x, y),
    ]
    base = [
        (x - r, y + r),
        (x + r, y + r),
        (x, y),
    ]
    pygame.draw.polygon(tela, AMARELO, topo)
    pygame.draw.polygon(tela, AMARELO, base)
    pygame.draw.polygon(tela, LARANJA, topo, 2)
    pygame.draw.polygon(tela, LARANJA, base, 2)
    pygame.draw.line(tela, LARANJA, (x - r, y - r), (x + r, y - r), 3)
    pygame.draw.line(tela, LARANJA, (x - r, y + r), (x + r, y + r), 3)


def desenhar_tela_inicial(tela, fonte_grande, fonte, botao_iniciar):
    """Desenha a tela inicial com o botao de iniciar."""
    desenhar_texto(tela, fonte_grande, "Alvo Relampago", VERMELHO_ESCURO, 235, 140)

    pygame.draw.rect(tela, AZUL, botao_iniciar)
    pygame.draw.rect(tela, PRETO, botao_iniciar, 3)
    desenhar_texto(tela, fonte, "Iniciar", BRANCO, 360, 268)

    desenhar_texto(tela, fonte, "Clique no alvo ate o tempo acabar.", PRETO, 205, 360)
    desenhar_texto(tela, fonte, "Tente conseguir o maximo de pontuacao possivel.", PRETO, 135, 400)


def desenhar_vidas(tela, vidas, x, y):
    """Desenha coracoes representando as vidas do jogador."""
    for i in range(vidas):
        cx = x + i * 28
        r = 8
        pygame.draw.circle(tela, ROSA, (cx - r // 2, y - r // 4), r // 2)
        pygame.draw.circle(tela, ROSA, (cx + r // 2, y - r // 4), r // 2)
        pts = [(cx - r, y - r // 4), (cx, y + r), (cx + r, y - r // 4)]
        pygame.draw.polygon(tela, ROSA, pts)


def desenhar_informacoes(tela, fonte, pontos, vidas, tempo_restante, recorde):
    """Desenha pontuacao, vidas, tempo, recorde e nivel."""
    nivel = calcular_nivel(pontos)

    desenhar_texto(tela, fonte, "Pontos: " + str(pontos), PRETO, 20, 20)
    desenhar_texto(tela, fonte, "Vidas:", PRETO, 190, 20)
    desenhar_vidas(tela, vidas, 265, 32)
    desenhar_texto(tela, fonte, "Tempo: " + str(tempo_restante), PRETO, 330, 20)
    desenhar_texto(tela, fonte, "Recorde: " + str(recorde) + " pts", PRETO, 500, 20)
    desenhar_texto(tela, fonte, "Nivel: " + nivel, AZUL, 20, 55)


def desenhar_tela_final(tela, fonte_grande, fonte, mensagem, pontos):
    """Mostra a tela final da partida."""
    nivel = calcular_nivel(pontos)

    desenhar_texto(tela, fonte_grande, mensagem, VERMELHO_ESCURO, 250, 235)
    desenhar_texto(tela, fonte, "Pontuacao final: " + str(pontos), PRETO, 285, 305)
    desenhar_texto(tela, fonte, "Nivel final: " + nivel, PRETO, 305, 345)
    desenhar_texto(tela, fonte, "Pressione ESPACO para jogar novamente", AZUL, 200, 390)
    desenhar_texto(tela, fonte, "Pressione ESC para sair", AZUL, 280, 430)


# ---------------------------------------------------------------------------
# Logica da partida
# ---------------------------------------------------------------------------

def reiniciar_partida():
    """Volta a partida para os valores iniciais."""
    pontos = 0
    vidas = VIDAS_INICIAIS
    alvo_x, alvo_y, tamanho_alvo = criar_alvo(pontos)
    inicio = pygame.time.get_ticks()
    jogando = True
    mensagem = ""

    # Estado dos itens especiais: cada item e um dicionario com posicao,
    # tempo de surgimento e se esta ativo
    coracao = {"ativo": False, "x": 0, "y": 0, "surgiu_em": 0}
    ampulheta = {"ativo": False, "x": 0, "y": 0, "surgiu_em": 0}

    # Guarda o momento (em ms) em que cada item deve aparecer pela proxima vez
    proximo_coracao = pygame.time.get_ticks() + sortear_proximo_intervalo(INTERVALO_ITEM_MIN, INTERVALO_ITEM_MAX) * 1000
    proxima_ampulheta = pygame.time.get_ticks() + sortear_proximo_intervalo(INTERVALO_ITEM_MIN, INTERVALO_ITEM_MAX) * 1000

    return (
        pontos, vidas, alvo_x, alvo_y, tamanho_alvo,
        inicio, jogando, mensagem,
        coracao, ampulheta,
        proximo_coracao, proxima_ampulheta,
    )


def verificar_fim_da_partida(pontos, vidas, tempo_restante):
    """Verifica se a partida acabou."""
    if jogador_perdeu(vidas):
        return False, "Fim de jogo"

    if tempo_acabou(tempo_restante):
        return False, "Tempo esgotado"

    return True, ""


def atualizar_item(item, proximo_surgimento, agora, duracao):
    """
    Verifica se um item deve surgir ou expirar.
    Retorna o item e o proximo_surgimento atualizados.
    """
    if not item["ativo"]:
        if agora >= proximo_surgimento:
            x, y = criar_posicao_item()
            item = {"ativo": True, "x": x, "y": y, "surgiu_em": agora}
    else:
        if item_expirou(item["surgiu_em"], agora, duracao):
            item = {"ativo": False, "x": 0, "y": 0, "surgiu_em": 0}
            proximo_surgimento = agora + sortear_proximo_intervalo(INTERVALO_ITEM_MIN, INTERVALO_ITEM_MAX) * 1000

    return item, proximo_surgimento


def desativar_item(item):
    """Marca o item como inativo apos ser coletado."""
    return {"ativo": False, "x": 0, "y": 0, "surgiu_em": 0}


# ---------------------------------------------------------------------------
# Loop principal
# ---------------------------------------------------------------------------

def executar_jogo():
    """Executa o jogo Alvo Relampago."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    fonte = pygame.font.SysFont("arial", 28)
    fonte_grande = pygame.font.SysFont("arial", 48, bold=True)

    recorde = carregar_recorde(CAMINHO_RECORDE)

    # Estado inicial antes de comecar
    pontos = 0
    vidas = VIDAS_INICIAIS
    alvo_x, alvo_y, tamanho_alvo = criar_alvo(pontos)
    inicio = 0
    jogando = False
    mensagem = ""
    tempo_restante = TEMPO_LIMITE
    tela_inicial = True
    botao_iniciar = pygame.Rect(300, 250, 200, 70)
    coracao = {"ativo": False, "x": 0, "y": 0, "surgiu_em": 0}
    ampulheta = {"ativo": False, "x": 0, "y": 0, "surgiu_em": 0}
    proximo_coracao = 0
    proxima_ampulheta = 0
    rodando = True

    while rodando:
        agora = pygame.time.get_ticks()
        relogio.tick(FPS)

        if jogando:
            segundos_passados = (agora - inicio) // 1000
            tempo_restante = calcular_tempo_restante(TEMPO_LIMITE, segundos_passados)

            # Atualiza itens especiais
            coracao, proximo_coracao = atualizar_item(coracao, proximo_coracao, agora, DURACAO_ITEM)
            ampulheta, proxima_ampulheta = atualizar_item(ampulheta, proxima_ampulheta, agora, DURACAO_ITEM)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

                if evento.key == pygame.K_SPACE and tela_inicial:
                    (pontos, vidas, alvo_x, alvo_y, tamanho_alvo,
                     inicio, jogando, mensagem,
                     coracao, ampulheta,
                     proximo_coracao, proxima_ampulheta) = reiniciar_partida()
                    tela_inicial = False

                elif evento.key == pygame.K_SPACE and not jogando and not tela_inicial:
                    (pontos, vidas, alvo_x, alvo_y, tamanho_alvo,
                     inicio, jogando, mensagem,
                     coracao, ampulheta,
                     proximo_coracao, proxima_ampulheta) = reiniciar_partida()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if tela_inicial and botao_iniciar.collidepoint(evento.pos):
                    (pontos, vidas, alvo_x, alvo_y, tamanho_alvo,
                     inicio, jogando, mensagem,
                     coracao, ampulheta,
                     proximo_coracao, proxima_ampulheta) = reiniciar_partida()
                    tela_inicial = False

                elif jogando:
                    raio_atual = obter_raio_alvo(tamanho_alvo)

                    # Verifica coracao primeiro
                    if coracao["ativo"] and item_foi_clicado(evento.pos, (coracao["x"], coracao["y"])):
                        vidas = curar_vida(vidas)
                        coracao = desativar_item(coracao)
                        proximo_coracao = agora + sortear_proximo_intervalo(INTERVALO_ITEM_MIN, INTERVALO_ITEM_MAX) * 1000

                    # Verifica ampulheta
                    elif ampulheta["ativo"] and item_foi_clicado(evento.pos, (ampulheta["x"], ampulheta["y"])):
                        inicio += BONUS_TEMPO * 1000
                        ampulheta = desativar_item(ampulheta)
                        proxima_ampulheta = agora + sortear_proximo_intervalo(INTERVALO_ITEM_MIN, INTERVALO_ITEM_MAX) * 1000

                    # Verifica alvo
                    elif clique_acertou_alvo(evento.pos, (alvo_x, alvo_y), raio_atual):
                        pontos_ganhos = obter_pontos_alvo(tamanho_alvo)
                        pontos = calcular_pontos(pontos, pontos_ganhos)
                        alvo_x, alvo_y, tamanho_alvo = criar_alvo(pontos)

                    else:
                        vidas = tomar_dano(vidas, 1)

        if jogando:
            jogando, mensagem = verificar_fim_da_partida(pontos, vidas, tempo_restante)

            novo_recorde = atualizar_recorde(pontos, recorde)
            if novo_recorde != recorde:
                recorde = novo_recorde
                salvar_recorde(CAMINHO_RECORDE, recorde)

        # --- Renderizacao ---
        tela.fill(CINZA)

        if tela_inicial:
            desenhar_tela_inicial(tela, fonte_grande, fonte, botao_iniciar)
        else:
            desenhar_informacoes(tela, fonte, pontos, vidas, tempo_restante, recorde)

            if jogando:
                raio_atual = obter_raio_alvo(tamanho_alvo)
                desenhar_alvo(tela, alvo_x, alvo_y, raio_atual)

                if coracao["ativo"]:
                    desenhar_coracao(tela, coracao["x"], coracao["y"])

                if ampulheta["ativo"]:
                    desenhar_ampulheta(tela, ampulheta["x"], ampulheta["y"])
            else:
                desenhar_tela_final(tela, fonte_grande, fonte, mensagem, pontos)

        pygame.display.flip()

    pygame.quit()
