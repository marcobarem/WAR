# Questão 1
## Minimax para Jogo da Velha

Este projeto implementa uma IA para jogar o jogo da velha utilizando o algoritmo de busca Minimax. O objetivo é criar um jogador capaz de escolher a jogada ideal a cada turno, maximizando suas chances de vitória e minimizando as chances de derrota.
Estado Inicial do Tabuleiro

O tabuleiro inicial para esta questão é configurado como:
```
 X |   |   
-----------
   | O |   
-----------
   |   | X

```
Onde:

    * X representa o jogador inicial.
    * O é o adversário.

### Objetivo

Implementar uma IA que tome decisões no jogo da velha usando o algoritmo Minimax para identificar a jogada ideal.
Perguntas e Soluções

    -Qual é a profundidade máxima que você deve definir para a busca Minimax neste caso?
        A profundidade máxima da busca é 6 movimentos, pois há 6 espaços vazios restantes no tabuleiro.

    -Qual é a próxima jogada para o jogador X?
        A IA utilizará o Minimax para avaliar todas as posições disponíveis e escolher a que maximiza suas chances de vitória ou evita derrota.

    -E se o jogador X fizer uma jogada subótima, qual é a melhor jogada que o jogador O pode
fazer em seguida?
        Se X jogar subotimamente, o jogador O aplicará o Minimax para escolher a melhor jogada que maximize suas próprias chances ou bloqueie X.

    -Suponha que o jogador O faça uma jogada subótima. Qual seria a consequência disso na
próxima jogada de X?
        Caso O jogue subotimamente, X aplicará o Minimax para explorar a fraqueza e potencialmente garantir uma vitória.    


# Questão 2:

## Busca A* para Resolver um Labirinto

Este projeto aplica o algoritmo de busca A* para resolver um labirinto, onde um robô deve encontrar o caminho mais curto da posição inicial ("E") até a posição de saída ("S"). O algoritmo A* é ideal para este problema, pois encontra o caminho mais eficiente, minimizando o custo dos movimentos.
Descrição do Problema

- No labirinto, o robô:

    Começa na célula marcada como "E".
    Seu objetivo é alcançar a saída marcada como "S".
    Pode mover-se apenas nas direções cima, baixo, esquerda e direita.
    Não pode atravessar paredes ou bordas do labirinto.

- Formatação em Problema de Busca

    Espaço de Estados: Cada célula acessível no labirinto é um estado possível.
    Estado Inicial: A posição inicial do robô, indicada pela letra E.
    Estado Final: A posição da saída, indicada pela letra S.
    Operadores de Transição: Movimentos nas quatro direções (cima, baixo, esquerda, direita), desde que não sejam bloqueados por uma parede ou borda.
    Custo: Cada movimento tem um custo uniforme, então o A* visa encontrar o menor número de passos para alcançar o objetivo.

## Representação em Grafo

Para aplicar A*, o labirinto é representado como um grafo, onde:

    Cada célula acessível representa um nó.
    Cada conexão entre células adjacentes é uma aresta com um custo fixo.

Implementação do Algoritmo A*
Estrutura do Algoritmo

O A* utiliza uma função de avaliação f(n) = g(n) + h(n), onde:

    g(n): Custo do caminho do estado inicial até o estado atual n.
    h(n): Heurística que estima o custo do estado atual n até o estado final. A heurística usada é a distância de Manhattan, calculada como:

h(n)=∣Xatual−Xdestino∣+∣Yatual−Ydestino∣
h(n)=∣Xatual​−Xdestino​∣+|Yatual​−Ydestino​∣        

## Exemplo de implementação em Python

```
import heapq

def a_star(labirinto, inicio, destino):
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (0, inicio))
    custos = {inicio: 0}
    caminhos = {inicio: None}
    
    while fila_prioridade:
        _, atual = heapq.heappop(fila_prioridade)
        
        if atual == destino:
            break
        
        for vizinho in obter_vizinhos(labirinto, atual):
            novo_custo = custos[atual] + 1  # Custo uniforme
            if vizinho not in custos or novo_custo < custos[vizinho]:
                custos[vizinho] = novo_custo
                prioridade = novo_custo + heuristica_manhattan(vizinho, destino)
                heapq.heappush(fila_prioridade, (prioridade, vizinho))
                caminhos[vizinho] = atual
    
    return reconstruir_caminho(caminhos, inicio, destino)

def heuristica_manhattan(atual, destino):
    return abs(atual[0] - destino[0]) + abs(atual[1] - destino[1])

def obter_vizinhos(labirinto, posicao):
    # Função para obter vizinhos válidos (cima, baixo, esquerda, direita)
    pass

def reconstruir_caminho(caminhos, inicio, destino):
    # Função para reconstruir o caminho do início ao destino
    pass

```

Explicação do Código

    -*a_star*: Função principal que implementa o A*.
    -*heuristica_manhattan*: Calcula a distância de Manhattan entre o estado atual e o destino.
    -*obter_vizinhos*: Retorna vizinhos válidos ao redor da posição atual.
    -*reconstruir_caminho*: Traça o caminho do destino até o início.