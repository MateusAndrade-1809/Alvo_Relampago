# Alvo Relampago

Projeto final da disciplina de Introducao a Algoritmos/Programacao, desenvolvido com Python e Pygame.

## Integrantes do grupo

- Daniel Viana
- Rodrigo Ventura
- Luiz Moura
- Mateus Andrade
- Arthur Ramos

## Descricao do jogo

Alvo Relampago e um jogo simples de clique rapido. Um alvo circular aparece em uma posicao aleatoria da tela, e o jogador deve clicar nele para ganhar pontos. Quando o jogador erra o alvo, perde uma vida.

Na Semana 3, o jogo ganhou tempo limite, sistema de niveis, condicao de derrota e recorde salvo em arquivo.

## Objetivo do jogador

O objetivo e fazer a maior pontuacao possivel antes que o tempo acabe ou antes de perder todas as vidas.

## Regras do jogo

- O jogador comeca com 3 vidas.
- Cada clique correto no alvo aumenta 5 pontos.
- Cada clique fora do alvo remove 1 vida.
- Depois de um acerto, o alvo muda para uma nova posicao aleatoria.
- O jogador perde se as vidas chegarem a zero.
- O jogador tambem perde se o tempo acabar.
- O jogo mostra o nivel do jogador de acordo com a pontuacao.
- O maior recorde fica salvo em `data/recorde.txt`.

## Niveis de pontuacao

- 0 a 95 pontos: Iniciante.
- 100 a 245 pontos: Intermediario.
- 250 a 395 pontos: Excelente.
- 400 a 595 pontos: Extraordinario.
- 600 pontos ou mais: Deus.

## Controles

- Botao Iniciar: comeca a partida.
- Mouse: clicar no alvo.
- Espaco: iniciar ou reiniciar depois do fim da partida.
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
- Tela inicial com botao Iniciar e descricao do jogo.
- Alvo clicavel aparecendo na tela.
- Pontuacao e vidas funcionando.
- Tempo limite funcionando.
- Tela final com resultado e nivel do jogador.
- Reinicio da partida com ESPACO.
- Saida do jogo com ESC.
- Recorde salvo em arquivo.
- Codigo organizado em funcoes simples.
- Testes automatizados para a logica principal.
