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
    linhas, colunas = len(labirinto), len(labirinto[0])
    x, y = posicao
    vizinhos = []
    
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # cima, baixo, esquerda, direita
    
    for dx, dy in movimentos:
        nx, ny = x + dx, y + dy
        # Verifica se o vizinho está dentro dos limites e não é uma parede
        if 0 <= nx < linhas and 0 <= ny < colunas and labirinto[nx][ny] != 1:
            vizinhos.append((nx, ny))
    
    return vizinhos

def reconstruir_caminho(caminhos, inicio, destino):
    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = caminhos[atual]
    caminho.reverse()  # Inverte o caminho para começar do início
    return caminho if caminho[0] == inicio else None

```

Explicação do Código

    -*a_star*: Função principal que implementa o A*.
    -*heuristica_manhattan*: Calcula a distância de Manhattan entre o estado atual e o destino.
    -*obter_vizinhos*: Retorna vizinhos válidos ao redor da posição atual.
    -*reconstruir_caminho*: Traça o caminho do destino até o início.

# Questão 3:

## Implementação de IA para o Jogo WAR

Este projeto se baseia na modelagem de componentes de IA para o jogo de estratégia WAR. Utilizaremos os conceitos de descrições de estado, geradores de movimento, testes de terminal, funções de utilidade e funções de avaliação para definir e implementar um agente inteligente que possa tomar decisões estratégicas no jogo.
Descrição do Jogo WAR

WAR é um jogo de estratégia em que os jogadores competem para conquistar territórios e eliminar exércitos adversários. Cada jogador começa com um número de territórios e unidades militares e deve escolher cuidadosamente onde atacar e reforçar.
Componentes de Busca para o Jogo WAR
1. Descrição do Estado

No jogo WAR, um estado representa a situação atual do tabuleiro, incluindo:

    Territórios ocupados: Quais territórios pertencem a cada jogador.
    Exércitos em cada território: Número de tropas em cada território controlado.
    Objetivos secretos e conquistas: Cada jogador pode ter objetivos próprios, o que também influencia a estratégia da IA.

2. Geradores de Movimento

O gerador de movimento define as ações que a IA pode tomar em cada turno. Em WAR, as ações podem incluir:

    Ataque: A IA pode atacar territórios vizinhos ocupados por oponentes, desde que tenha tropas suficientes para um ataque (mínimo de 2 tropas).
    Reforço: Redistribuir ou adicionar tropas aos territórios ocupados no início do turno.
    Movimento: Mover tropas entre territórios próprios adjacentes para fortalecer fronteiras.

Para cada ação, a IA avalia as probabilidades de sucesso com base nas tropas de ataque e defesa e escolhe as ações mais vantajosas de acordo com sua função de avaliação.
3. Teste de Terminal

O teste de terminal determina quando o jogo termina, ou seja, quando um jogador alcança seu objetivo ou conquista todos os territórios:

    Vitória: A IA atinge seu objetivo secreto ou conquista o mundo inteiro.
    Derrota: A IA é eliminada ou perde todos os seus territórios.

4. Função de Utilidade

A função de utilidade é usada para medir a "vantagem" do estado atual para a IA. Para o jogo WAR, a função de utilidade pode considerar:

    Número de territórios controlados: Mais territórios representam mais poder.
    Distribuição de tropas: Estados com maior número de tropas são mais vantajosos.
    Proximidade aos objetivos: O progresso em direção ao objetivo secreto aumenta o valor do estado.    

 Exemplo de Função de Utilidade:
U(s)=(T×w1)+(P×w2)+(O×w3)
U(s)=(T×w1​)+(P×w2​)+(O×w3​)

onde:

    TT = número de territórios controlados
    PP = número total de tropas
    OO = proximidade ao objetivo secreto
    w1,w2,w3w1​,w2​,w3​ = pesos para balancear cada fator de acordo com a estratégia desejada

5. Função de Avaliação

A função de avaliação ajuda a IA a escolher entre diferentes estados intermediários antes do fim do jogo. Em WAR, ela avalia estados considerando:

    Força relativa: Avalia o poder militar da IA em comparação com seus oponentes.
    Posição estratégica: Priorização de territórios que são adjacentes a territórios controlados por oponentes.
    Conquista de Continentes: Completar a posse de um continente garante bônus, o que aumenta o valor estratégico.   