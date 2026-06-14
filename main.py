import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from src.jogo import executar_jogo


if __name__ == "__main__":
    # Ponto de entrada do jogo.
    executar_jogo()
