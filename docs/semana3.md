# Semana 3 - Alvo Relampago

## O que foi implementado

Na Semana 3, o prototipo da Semana 2 foi melhorado com regras de partida mais completas.

## Funcionalidades

- Tempo limite de 30 segundos.
- Tela inicial com botao Iniciar.
- Descricao breve explicando que o jogador deve clicar no alvo e fazer a maior pontuacao possivel.
- Derrota ao perder todas as vidas.
- Derrota quando o tempo acaba.
- Pontuacao aumentada para 5 pontos por acerto.
- Nivel do jogador de acordo com a pontuacao.
- Tela final com mensagem de resultado.
- Reinicio da partida usando a tecla ESPACO.
- Saida do jogo usando a tecla ESC.
- Recorde salvo no arquivo `data/recorde.txt`.
- Codigo refeito de forma mais simples, usando variaveis e funcoes pequenas.

## Como testar manualmente

1. Execute `python main.py`.
2. Clique no botao Iniciar.
3. Clique no alvo vermelho para ganhar pontos.
4. Clique fora do alvo para perder vidas.
5. Tente fazer a maior pontuacao possivel antes do tempo acabar.
6. Quando a partida terminar, pressione ESPACO para reiniciar.
7. Pressione ESC para sair.

## Niveis

- 0 a 95 pontos: Iniciante.
- 100 a 245 pontos: Intermediario.
- 250 a 395 pontos: Excelente.
- 400 a 595 pontos: Extraordinario.
- 600 pontos ou mais: Deus.

## Como testar automaticamente

```bash
python -m pytest
```
