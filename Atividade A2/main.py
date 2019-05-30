"""
Usage: main.py (<arquivoDeGrafo>) [options]
          main.py -h | --help

Options:
  -h --help     se nao especificado, chamam-se todas as funcoes (com vertice inicial 1)
  -v vertice    indica numero vertice inicial
  -l            executa Busca em Largura (requer opção -v)
  -e            busca ciclo euleriano e o retorna
  -d            executa algoritmo de Dijkstra a partir do vertice inicial (requer opção -v)
  -f            executa algoritmo de Floyd-Warshall
"""
import Algoritmos
from Grafo import Grafo
import pprint
from docopt import docopt


def check_args(args):
    if (not ['<arquivoDeGrafo>']):
        exit("(<arquivoDeGrafo>) é necessário!\
                \n Use '-h' para ajuda")
    selecionaAlgoritmos(args)


def selecionaAlgoritmos(args):
    grafo = Grafo(args['<arquivoDeGrafo>'])
    vertice = int(args['-v'] or 1)
    executaTodos = not(args['-l'] or args['-e'] or args['-d'] or args['-f'])

    if args['-l'] or executaTodos:
        print("\nExecutando Busca em Largura a partir do vertice", vertice)
        Algoritmos.buscaEmLargura(grafo, vertice)
    if args['-e'] or executaTodos:
        print("\nBuscando Ciclo Euleriano")
        Algoritmos.algoritmoDeHierholzer(grafo)
    if args['-d'] or executaTodos:
        print("\nExecutando Djikstra a partir do vertice", vertice)
        Algoritmos.dijkstra(grafo, vertice)
    if args['-f'] or executaTodos:
        print("\nExecutando Floyd-Warshall")
        Algoritmos.floydWarshall(grafo)


# if __name__ == '__main__':
#     args = docopt(__doc__)
#     check_args(args)


g = Grafo("dolphins.net")
# gt = g.getGrafoTransposto()
# gtt = gt.getGrafoTransposto()
# pp = pprint.PrettyPrinter(indent=2)
# pp.pprint(gtt.arestas == g.arestas)
A = Algoritmos.prim(g)
print(A)
