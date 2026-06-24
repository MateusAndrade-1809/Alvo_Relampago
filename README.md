# Alvo Relâmpago

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido
com Python e Pygame.

## Integrantes do grupo

- Daniel Viana
- Rodrigo Ventura
- Luiz Moura
- Mateus Andrade
- Arthur Ramos

## Sobre o jogo

Alvo Relâmpago é um jogo de precisão e velocidade. O jogador precisa acertar
alvos que aparecem em posições aleatórias antes que eles desapareçam. Conforme
a pontuação aumenta, os alvos ficam menores, passam a se mover e permanecem
menos tempo na tela.

O jogo possui cadastro e seleção de jogadores, ranking Top 5, recorde local,
itens especiais, efeitos sonoros, feedback visual e estatísticas da partida.

## Regras

- O jogador começa com 3 vidas e 30 segundos.
- Acertar um alvo concede pontos de acordo com o tamanho dele.
- Clicar fora do alvo remove uma vida.
- Deixar um alvo desaparecer também remove uma vida.
- A partida termina quando o tempo acaba ou as vidas chegam a zero.
- O coração recupera uma vida, respeitando o limite de 3.
- A ampulheta adiciona 5 segundos ao tempo restante.
- Alvos e itens nunca são criados sobrepostos.

## Pontuação dos alvos

| Tamanho | Pontos |
|---|---:|
| Grande | 4 |
| Médio | 5 |
| Pequeno | 8 |
| Mínimo | 12 |

## Dificuldade progressiva

| Pontuação | Fase | Comportamento |
|---:|---|---|
| 0 | Aquecimento | Alvos grandes ou médios |
| 40 | Ágil | Alvos médios ou pequenos |
| 100 | Rápido | Alvos começam a se mover |
| 250 | Relâmpago | Alvos menores, rápidos e com menos tempo |

## Níveis de desempenho

- 0 a 99 pontos: Iniciante
- 100 a 249 pontos: Intermediário
- 250 a 399 pontos: Excelente
- 400 a 599 pontos: Extraordinário
- 600 pontos ou mais: Deus

## Controles

- Digitação: informa o nome do jogador.
- Enter ou botão **Iniciar**: começa a partida.
- Mouse: acerta alvos e coleta itens.
- Espaço: inicia uma nova partida após o fim.
- Esc: fecha o jogo.

## Ranking e estatísticas

As cinco melhores pontuações são salvas em `data/ranking.txt`. A tela final
mostra:

- acertos;
- erros;
- alvos perdidos;
- precisão;
- itens coletados;
- tempo jogado;
- nível final;
- ranking Top 5.

## Como executar

Requer Python instalado. Na pasta do projeto:

```bash
python -m pip install -r requirements.txt
python main.py
```

O `requirements.txt` instala automaticamente a edição do Pygame compatível com
a versão do Python utilizada.

## Como executar os testes

```bash
python -m pytest
```

## Estrutura do projeto

- `main.py`: ponto de entrada.
- `src/jogo.py`: loop principal, eventos e renderização.
- `src/estado.py`: estado da partida, alvo, itens e estatísticas.
- `src/funcoes.py`: regras e funções testáveis.
- `src/dados.py`: recorde, jogadores e ranking.
- `src/audio.py`: efeitos sonoros gerados em memória.
- `src/config.py`: configurações, cores e balanceamento.
- `tests/`: testes automatizados.
- `docs/`: documentação da disciplina.
- `assets/`: documentação dos recursos visuais e sonoros.
- `data/`: persistência local do recorde e ranking.

## Dados locais

- `data/recorde.txt`: maior pontuação registrada.
- `data/ranking.txt`: Top 5 no formato `nome;pontuação`.

Os elementos visuais são desenhados pelo Pygame e os efeitos sonoros são
gerados pelo próprio código. O projeto não depende de imagens ou áudios
externos.
