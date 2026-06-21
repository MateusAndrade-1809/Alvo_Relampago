# Configuracoes principais do jogo.
LARGURA_TELA = 800
ALTURA_TELA = 600
FPS = 60

TITULO_JOGO = "Alvo Relampago"

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (224, 229, 236)
VERMELHO = (220, 45, 45)
VERMELHO_ESCURO = (145, 22, 22)
AZUL = (34, 92, 172)
VERDE = (30, 140, 80)
ROSA = (220, 80, 120)
AMARELO = (230, 180, 30)
LARANJA = (220, 110, 30)

RAIO_ALVO = 35
VIDAS_INICIAIS = 3
VIDAS_MAXIMAS = 3
PONTOS_POR_ACERTO = 5

TEMPO_LIMITE = 30
BONUS_TEMPO = 5

# Tamanhos de alvo: (raio, pontos_por_acerto)
TAMANHOS_ALVO = {
    "medio":   {"raio": 30, "pontos": 5},
    "pequeno": {"raio": 18, "pontos": 8},
}
PONTUACAO_PARA_VARIAR_ALVO = 10

# Itens especiais
DURACAO_ITEM = 5        # segundos que o item fica na tela
INTERVALO_ITEM_MIN = 6  # segundos minimos entre aparicoes de cada item
INTERVALO_ITEM_MAX = 12 # segundos maximos entre aparicoes de cada item
RAIO_ITEM = 20

CAMINHO_RECORDE = "data/recorde.txt"
