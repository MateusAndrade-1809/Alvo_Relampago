# Alvo Relampago

Projeto final da disciplina de Introducao a Algoritmos/Programacao, desenvolvido com Python e Pygame.

## Integrantes do grupo

- Daniel Viana
- Rodrigo
- Luiz Moura
- Mateus Andrade

## Descricao do jogo

Alvo Relampago e um jogo simples de clique rapido. Um alvo circular aparece em uma posicao aleatoria da tela, e o jogador deve clicar nele para ganhar pontos. Quando o jogador erra o alvo, perde uma vida.

O jogo tem tela inicial, tempo limite, sistema de pontuacao, vidas, niveis por desempenho, recorde salvo em arquivo e tela final.

## Objetivo do jogador

O objetivo e fazer a maior pontuacao possivel antes que o tempo acabe ou antes de perder todas as vidas.

## Regras do jogo

- O jogador comeca com 3 vidas.
- Cada clique correto no alvo aumenta 5 pontos.
- Cada clique fora do alvo remove 1 vida.
- Depois de um acerto, o alvo muda para uma nova posicao aleatoria.
- A partida termina quando as vidas chegam a zero.
- A partida tambem termina quando o tempo acaba.
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
- `assets/`: arquivos de assets e referencias.
- `data/`: arquivos auxiliares de dados.

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

## Arquivos importantes

- `docs/proposta.md`: proposta inicial do jogo.
- `docs/semana3.md`: resumo das funcionalidades criadas ate a Semana 3.
- `docs/apresentacao.md`: roteiro para apresentacao em sala.
- `assets/REFERENCIAS.md`: referencias e observacoes sobre assets externos.
- `data/recorde.txt`: arquivo usado para salvar o recorde.

## Entrega final

- Jogo completo e executavel.
- Codigo-fonte organizado em modulos.
- README preenchido.
- Proposta inicial em `docs/proposta.md`.
- Testes implementados.
- Arquivos auxiliares em `data/`.
- Referencias de assets em `assets/REFERENCIAS.md`.
- Roteiro de apresentacao em `docs/apresentacao.md`.
