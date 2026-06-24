# Semana 4 – Evolução do Projeto

## Funcionalidades Implementadas

Durante a Semana 4 foram adicionadas novas mecânicas ao jogo **Alvo Relâmpago**

### 1. Item de Vida (Coração)

Foi implementado um item especial representado por um coração.

* O coração aparece aleatoriamente durante a partida.
* Ao clicar nele, o jogador recupera uma vida.
* O número máximo de vidas permanece limitado a 3.
* Caso o jogador já esteja com 3 vidas, o coração não aumenta esse valor.
* O item desaparece automaticamente após alguns segundos caso não seja coletado.

Essa funcionalidade adiciona uma nova estratégia ao jogo, permitindo que o jogador recupere vidas perdidas.

---

### 2. Alvos com Diferentes Tamanhos

Foi implementado um sistema de variação de tamanho dos alvos.

* Após o jogador atingir uma determinada quantidade de pontos, novos tamanhos de alvo passam a ser gerados.
* Os alvos podem aparecer em tamanhos diferentes, aumentando a diversidade das partidas.
* Alvos menores exigem maior precisão do jogador.
* O sistema mantém o posicionamento correto dos alvos dentro da área visível da tela.

Essa melhoria aumenta progressivamente a dificuldade do jogo.

---

### 3. Item de Tempo (Ampulheta)

Foi adicionado um item especial representado por uma ampulheta.

* A ampulheta surge aleatoriamente durante a partida.
* Ao clicar nela, o jogador recebe um bônus de +5 segundos no tempo restante.
* O item desaparece automaticamente após alguns segundos caso não seja coletado.
* Após desaparecer ou ser utilizado, uma nova ampulheta pode surgir posteriormente.

Essa mecânica oferece ao jogador a possibilidade de prolongar a partida e alcançar pontuações maiores.

---

## Benefícios das Melhorias

As funcionalidades implementadas nesta etapa contribuíram para:

* Tornar a jogabilidade mais dinâmica.
* Aumentar a variedade das partidas.
* Criar um sistema de progressão de dificuldade.
* Melhorar a experiência geral do jogador.

## Próximos Passos

As ideias de cadastro e seleção de jogadores e ranking de pontuações foram
implementadas na evolução seguinte do projeto.

O sistema de combo permanece apenas como uma possibilidade futura e não faz
parte da versão atual.
