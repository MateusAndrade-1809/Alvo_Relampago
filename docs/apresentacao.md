# Roteiro de Apresentação - Alvo Relâmpago

## 1. Ideia principal

O jogador precisa clicar rapidamente nos alvos antes que desapareçam. A partida
fica progressivamente mais difícil.

## 2. Objetivo

Fazer a maior pontuação possível antes do tempo acabar ou antes de perder as
três vidas.

## 3. Mecânicas

- Alvos de quatro tamanhos, com pontuações diferentes.
- Quatro fases de dificuldade.
- Alvos móveis nas fases avançadas.
- Coração que recupera uma vida.
- Ampulheta que adiciona cinco segundos.
- Perda de vida ao errar ou deixar um alvo escapar.
- Feedback visual e sonoro para cada ação.

## 4. Jogadores e ranking

O jogador digita seu nome ou seleciona um nome salvo. Ao fim da partida, a
pontuação pode entrar no ranking Top 5 armazenado em `data/ranking.txt`.

## 5. Estatísticas

A tela final mostra acertos, erros, alvos perdidos, precisão, itens coletados,
tempo jogado, nível final e ranking.

## 6. Organização do código

- `main.py`: inicia o jogo.
- `src/jogo.py`: controla telas, eventos e desenho.
- `src/estado.py`: representa o estado atual da partida.
- `src/funcoes.py`: concentra regras testáveis.
- `src/dados.py`: salva recorde e ranking.
- `src/audio.py`: gera os efeitos sonoros.
- `src/config.py`: guarda configurações e balanceamento.

## 7. Testes

Os testes verificam pontuação, dano, tempo, níveis, itens, dificuldade,
posicionamento sem sobreposição, estatísticas, recorde e ranking.

## 8. Execução

```bash
python -m pip install -r requirements.txt
python main.py
```
