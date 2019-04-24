# Como Usar

## Instalar docopt

    pip3 install docopt

## Uso do arquivo main.py

    main.py (arquivoDeGrafo) [options]

Options:

  -h --help     se nao especificado, chamam-se todas as funcoes (com vertice inicial 1)  
  -v vertice    indica numero vertice inicial  
  -l            executa Busca em Largura (requer opção -v)  
  -e            busca ciclo euleriano e o retorna  
  -d            executa algoritmo de Dijkstra a partir do vertice inicial (requer opção -v)

  ### Exemplo

    $ python3 main.py dolphins.net -l -v 2