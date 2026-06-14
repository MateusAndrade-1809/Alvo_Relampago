# Semana 3 - Alvo Relampago

## O que foi implementado

Na Semana 3, o prototipo da Semana 2 foi melhorado com regras de partida mais completas.

## Funcionalidades

- Tempo limite de 30 segundos.
- Vitoria ao atingir 10 pontos.
- Derrota ao perder todas as vidas.
- Derrota quando o tempo acaba antes da vitoria.
- Tela final com mensagem de resultado.
- Reinicio da partida usando a tecla ESPACO.
- Saida do jogo usando a tecla ESC.
- Recorde salvo no arquivo `data/recorde.txt`.
- Codigo refeito de forma mais simples, usando variaveis e funcoes pequenas.

## Como testar manualmente

1. Execute `python main.py`.
2. Clique no alvo vermelho para ganhar pontos.
3. Clique fora do alvo para perder vidas.
4. Tente chegar a 10 pontos antes do tempo acabar.
5. Quando a partida terminar, pressione ESPACO para reiniciar.
6. Pressione ESC para sair.

## Como testar automaticamente

```bash
python -m pytest
```
