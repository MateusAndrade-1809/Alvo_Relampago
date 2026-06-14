# Proposta Inicial do Jogo

## Nome provisório do jogo

Alvo Relampago.

## Integrantes do grupo

Daniel Viana, Rodrigo, Luiz Moura e Mateus Andrade.

## Tipo de jogo

Jogo de clique rapido.

## Descricao geral

O jogo Alvo Relampago sera um jogo simples desenvolvido em Python com a biblioteca Pygame. Nele, o jogador devera clicar rapidamente em alvos que aparecem em posicoes aleatorias na tela.

A cada alvo acertado, o jogador ganha pontos. Caso o jogador clique fora do alvo, perde uma vida. O jogo tera um tempo limite e ficara progressivamente mais dificil em versoes futuras, podendo reduzir o tamanho do alvo ou aumentar a velocidade com que ele muda de posicao.

A proposta e criar um jogo simples, funcional e jogavel, focando principalmente na organizacao do codigo, no uso dos conceitos estudados na disciplina e na implementacao correta das regras.

## Objetivo do jogador

O objetivo do jogador e acertar o maior numero possivel de alvos antes que o tempo acabe ou antes que suas vidas cheguem a zero.

Para vencer a partida, o jogador devera atingir uma pontuacao minima definida pelo grupo dentro do tempo disponivel. Exemplo: o jogador vence se fizer 30 pontos em ate 60 segundos.

## Regras principais

1. O jogador deve clicar nos alvos que aparecem na tela.
2. Cada clique correto no alvo aumenta a pontuacao.
3. Cada clique fora do alvo faz o jogador perder uma vida.
4. O alvo aparece em posicoes aleatorias da tela.
5. O jogo tera um tempo limite.
6. O jogador comeca com uma quantidade fixa de vidas.
7. A partida termina quando o jogador vence, perde todas as vidas ou quando o tempo acaba.
8. O recorde do jogador podera ser salvo em um arquivo.

## Condicao de vitoria

O jogador vence se alcancar a pontuacao minima definida antes do tempo acabar e antes de perder todas as vidas.

## Condicao de derrota ou encerramento

O jogador perde se suas vidas chegarem a zero antes de alcancar a pontuacao necessaria.

A partida tambem pode ser encerrada quando o tempo acabar. Nesse caso, se o jogador nao tiver alcancado a pontuacao minima, sera considerado derrota.

## Elementos previstos

- Janela principal do jogo.
- Alvo clicavel.
- Pontuacao atual.
- Quantidade de vidas.
- Tempo restante.
- Mensagem de vitoria.
- Mensagem de derrota.
- Recorde salvo em arquivo.
- Tela simples de inicio ou instrucoes.
- Tela final com resultado da partida.

## Controles previstos

- Mouse: clique com o botao esquerdo para tentar acertar o alvo.
- Tecla espaco: iniciar ou reiniciar a partida.
- Tecla ESC: sair do jogo.

## Estruturas de dados que poderao ser utilizadas

Dicionarios serao usados para guardar informacoes do jogador, como pontuacao, vidas e recorde.

Tuplas serao usadas para representar posicoes, cores e tamanhos.

Listas poderao armazenar possiveis posicoes dos alvos ou eventos do jogo.

Variaveis serao usadas para controlar tempo, estado da partida e dificuldade.

Funcoes serao utilizadas para organizar partes do jogo, como desenhar elementos, verificar clique, atualizar pontuacao e salvar recorde.

## Uso previsto de arquivos

O jogo podera utilizar o arquivo `recorde.txt` para salvar a maior pontuacao alcancada pelo jogador.

Quando o jogo iniciar, o programa podera ler o recorde salvo. Ao final da partida, se o jogador fizer uma pontuacao maior, o novo recorde sera gravado no arquivo.

## Testes planejados

1. Testar se o clique do mouse acertou ou nao o alvo.
2. Testar se a pontuacao aumenta corretamente apos um acerto.
3. Testar se o jogador perde vida ao clicar fora do alvo.
4. Testar se a condicao de vitoria funciona corretamente.
5. Testar se a condicao de derrota funciona corretamente.
6. Testar se o recorde e salvo e carregado corretamente.

## Principais dificuldades esperadas

1. Organizar o codigo em funcoes de forma clara.
2. Controlar corretamente o tempo da partida.
3. Fazer o alvo aparecer em posicoes aleatorias sem sair da tela.
4. Verificar corretamente se o clique do mouse acertou o alvo.
5. Salvar e carregar o recorde usando arquivo.
6. Criar testes simples para as funcoes de logica do jogo.

## Escopo minimo para a entrega final

O escopo minimo da entrega final sera um jogo funcional em Pygame contendo janela principal funcionando, alvo aparecendo na tela, clique do mouse funcionando, pontuacao sendo atualizada, sistema de vidas, tempo limite, condicao de vitoria, condicao de derrota, recorde salvo em arquivo, codigo organizado em funcoes, README preenchido, proposta inicial no arquivo `docs/proposta.md` e testes simples implementados.

Caso sobre tempo, o grupo podera adicionar melhorias, como sons, tela inicial mais bonita, aumento progressivo de dificuldade, efeitos visuais simples e ranking com mais de uma pontuacao.
