# Semana 4 - Evolução do Projeto

## Funcionalidades implementadas

Durante a Semana 4 foram adicionadas novas mecânicas ao jogo **Alvo Relâmpago**.

### 1. Item de vida (coração)

- O coração aparece aleatoriamente durante a partida.
- Ao clicar nele, o jogador recupera uma vida.
- O número máximo de vidas permanece limitado a 3.
- O item desaparece automaticamente após alguns segundos caso não seja coletado.

### 2. Alvos e dificuldade progressiva

- Novos tamanhos de alvo são liberados conforme a pontuação aumenta.
- Alvos menores exigem mais precisão e valem mais pontos.
- Nas fases avançadas, os alvos se movimentam e desaparecem mais rapidamente.
- Alvos e itens são posicionados sem sobreposição dentro da área visível.

### 3. Item de tempo (ampulheta)

- A ampulheta aparece aleatoriamente durante a partida.
- Ao clicar nela, o jogador recebe um bônus de 5 segundos.
- O item desaparece automaticamente após alguns segundos caso não seja coletado.
- Depois de desaparecer ou ser utilizado, ele pode surgir novamente.

### 4. Cadastro e seleção de jogadores

- O jogador pode digitar um nome antes de começar.
- Nomes presentes no ranking podem ser selecionados na tela inicial.
- A partida e suas estatísticas ficam associadas ao jogador escolhido.

### 5. Ranking de pontuações

- As cinco melhores pontuações ficam salvas em `data/ranking.txt`.
- O ranking é ordenado da maior para a menor pontuação.
- As melhores colocações aparecem nas telas inicial e final.

### 6. Sistema de combo

- Cada acerto consecutivo aumenta o combo.
- A cada 3 acertos, o multiplicador de pontos aumenta em 1.
- O multiplicador máximo é 5.
- Um clique errado ou um alvo perdido zera o combo.
- O combo atual aparece durante a partida e o maior combo aparece na tela final.

## Outras melhorias concluídas

- Feedback visual e sonoro para acertos, erros e itens.
- Estatísticas de precisão, alvos perdidos, itens coletados e tempo jogado.
- Modos de janela, janela cheia e tela cheia.
- Testes automatizados para as regras e os fluxos principais.

## Benefícios das melhorias

- Jogabilidade mais dinâmica e variada.
- Progressão de dificuldade e recompensa por precisão.
- Partidas identificadas por jogador.
- Competição por meio de um ranking persistente.
- Incentivo a sequências de acertos com o sistema de combo.
