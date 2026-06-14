# Alvo Relampago

Projeto final da disciplina de Introducao a Algoritmos/Programacao, desenvolvido com Python e Pygame.

## Integrantes do grupo

- Daniel Viana
- Rodrigo
- Luiz Moura
- Mateus Andrade

## Descricao do jogo

Alvo Relampago e um jogo simples de clique rapido. Um alvo circular aparece em uma posicao aleatoria da tela, e o jogador deve clicar nele para ganhar pontos. Quando o jogador erra o alvo, perde uma vida.

Na Semana 3, o jogo ganhou tempo limite, condicao de vitoria, condicao de derrota e recorde salvo em arquivo.

## Objetivo do jogador

O objetivo e fazer 10 pontos antes que o tempo acabe e antes de perder todas as vidas.

## Regras do jogo

- O jogador comeca com 3 vidas.
- Cada clique correto no alvo aumenta 1 ponto.
- Cada clique fora do alvo remove 1 vida.
- Depois de um acerto, o alvo muda para uma nova posicao aleatoria.
- O jogador vence quando chega a 10 pontos.
- O jogador perde se as vidas chegarem a zero.
- O jogador tambem perde se o tempo acabar antes de atingir a pontuacao de vitoria.
- O maior recorde fica salvo em `data/recorde.txt`.

## Controles

- Mouse: clicar no alvo.
- Espaco: reiniciar depois do fim da partida.
- ESC: sair do jogo.

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicacao.
- `src/config.py`: configuracoes do jogo.
- `src/funcoes.py`: funcoes de logica.
- `src/dados.py`: leitura e escrita do recorde.
- `src/jogo.py`: janela, loop principal e desenho do jogo.
- `tests/`: testes unitarios.
- `docs/`: documentacao do projeto.

## Como executar o projeto

```bash
cd Alvo_Relampago
python -m pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Entrega da Semana 3

- Janela do Pygame funcionando.
- Loop principal funcionando.
- Alvo clicavel aparecendo na tela.
- Pontuacao e vidas funcionando.
- Tempo limite funcionando.
- Tela final de vitoria ou derrota.
- Reinicio da partida com ESPACO.
- Saida do jogo com ESC.
- Recorde salvo em arquivo.
- Codigo organizado em funcoes simples.
- Testes automatizados para a logica principal.
