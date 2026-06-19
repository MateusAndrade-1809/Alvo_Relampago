# Roteiro de Apresentacao - Alvo Relampago

## 1. Nome do jogo

Alvo Relampago.

## 2. Ideia principal

O jogador precisa clicar rapidamente nos alvos vermelhos que aparecem em posicoes aleatorias na tela.

## 3. Objetivo

Fazer a maior pontuacao possivel antes do tempo acabar ou antes de perder todas as vidas.

## 4. Controles

- Clique no botao Iniciar para comecar.
- Clique com o mouse no alvo para ganhar pontos.
- Clique fora do alvo perde uma vida.
- Espaco reinicia a partida depois do fim.
- ESC sai do jogo.

## 5. Regras

- O jogador comeca com 3 vidas.
- Cada acerto vale 5 pontos.
- Cada erro tira 1 vida.
- O tempo limite e de 30 segundos.
- O recorde fica salvo localmente em `data/recorde.txt`, por exemplo `Recorde: 100 pontos`.

## 6. Niveis

- Iniciante.
- Intermediario.
- Excelente.
- Extraordinario.
- Deus, a partir de 600 pontos.

## 7. Partes do codigo

- `main.py` inicia o jogo.
- `src/jogo.py` contem a janela, o loop principal e os desenhos.
- `src/funcoes.py` contem a logica de pontuacao, vidas, tempo e niveis.
- `src/dados.py` salva e carrega o recorde.
- `src/config.py` guarda configuracoes como tamanho da tela, cores e tempo.

## 8. Testes

Os testes verificam pontuacao, dano, derrota, tempo, niveis, clique no alvo e leitura/escrita do recorde.
