# Configuracoes principais do jogo.
LARGURA_TELA = 800
ALTURA_TELA = 600
FPS = 60
ALTURA_HUD = 100

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

VIDAS_INICIAIS = 3
VIDAS_MAXIMAS = 3

TEMPO_LIMITE = 30
BONUS_TEMPO = 5

# Tamanhos de alvo: (raio, pontos_por_acerto)
TAMANHOS_ALVO = {
    "grande": {"raio": 36, "pontos": 4},
    "medio": {"raio": 30, "pontos": 5},
    "pequeno": {"raio": 20, "pontos": 8},
    "minimo": {"raio": 14, "pontos": 12},
}

# Fases progressivas: alvos menores, menos tempo e movimento mais rapido.
FASES_DIFICULDADE = (
    {
        "pontos_minimos": 0,
        "nome": "Aquecimento",
        "tamanhos": ("grande", "medio"),
        "duracao_alvo": 3.0,
        "velocidade": 0,
    },
    {
        "pontos_minimos": 40,
        "nome": "Agil",
        "tamanhos": ("medio", "pequeno"),
        "duracao_alvo": 2.5,
        "velocidade": 0,
    },
    {
        "pontos_minimos": 100,
        "nome": "Rapido",
        "tamanhos": ("medio", "pequeno"),
        "duracao_alvo": 2.0,
        "velocidade": 80,
    },
    {
        "pontos_minimos": 250,
        "nome": "Relampago",
        "tamanhos": ("pequeno", "minimo"),
        "duracao_alvo": 1.5,
        "velocidade": 140,
    },
)

# Itens especiais
DURACAO_ITEM = 5        # segundos que o item fica na tela
INTERVALO_ITEM_MIN = 6  # segundos minimos entre aparicoes de cada item
INTERVALO_ITEM_MAX = 12 # segundos maximos entre aparicoes de cada item
RAIO_ITEM = 20
MARGEM_ENTRE_ELEMENTOS = 14

CAMINHO_RECORDE = "data/recorde.txt"
CAMINHO_RANKING = "data/ranking.txt"
LIMITE_RANKING = 5
LIMITE_NOME_JOGADOR = 16
