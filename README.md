# Como Usar

## Instalar docopt
  Pacote necessário para execução com parâmetros via terminal

    pip3 install docopt

## Uso do arquivo main.py

    main.py (arquivoDeGrafo) [options]

### Options (para Atividade A1):

  * **-h --help**: se não especificado, chamam-se todas as funções (com vértice inicial 1, quando necessário)
  * **-v vertice**: indica número do vértice inicial  
  * **-l**: executa Busca em Largura (requer opção -v)  
  * **-e**: busca ciclo euleriano e o retorna  
  * **-d**: executa algoritmo de Dijkstra a partir do vertice inicial (requer opção -v)

#### Exemplo

    $ python3 main.py dolphins.net -l -v 2

***

### Options (para Atividade A2):
  * **-h --help**: se não especificado, chamam-se todas as funções
  * **-c**: executa algoritmo de Componentes Fortemente Conexas (Kosaraju)  
  * **-o**: executa algoritmo de Ordenação Topológica 
  * **-a**: executa algoritmo de Árvore Geradora Mínima (Prim)

#### Exemplo

    $ python3 main.py dolphins.net -c

***

### Options (para Atividade A3):
  * **-h --help**: se não especificado, chamam-se todas as funções
  * **-s vertice**: indica número do vértice inicial
  * **-t vertice**: indica número do vértice final
  * **-f**: executa algoritmo de Fluxo Máximo (Edmonds-Karp)  
  * **-e**: executa algoritmo de Emparelhamento Máximo (Hopcroft-Karp) 
  * **-c**: executa algoritmo de Coloração de Vértices

#### Exemplo

    $ python3 main.py dolphins.net -s 2 -t 5 -f
