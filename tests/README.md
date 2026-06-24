# Testes

Esta pasta contem testes automatizados do projeto.

## Arquivos

- `test_logica.py`: valida pontuação, vidas, tempo, níveis e recorde.
- `test_melhorias.py`: valida dificuldade, itens, colisões, estatísticas e ranking.

## Como executar

```bash
python -m pytest
```

## Boas praticas

- Crie testes para toda regra de pontuação, vidas e condições de fim de jogo.
- Prefira funcoes pequenas e testaveis no modulo `src/funcoes.py`.
