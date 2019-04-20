"""
Usage: main.py (<arquivoDeGrafo>) [options]
          main.py -h | --help

Options:
  -h --help     se nao especificado, chamam-se todas as funcoes (com vertice inicial 1)
  -v vertice    indica numero vertice inicial
  -l            executa Busca em Largura (requer opção -v)
  -e            busca ciclo euleriano e o retorna
  -d            executa algoritmo de Dijkstra a partir do vertice inicial (requer opção -v)
"""
import Algoritmos
from Grafo import Grafo
from docopt import docopt


def check_args(args):
    if (not ['<arquivoDeGrafo>']):
        exit("(<arquivoDeGrafo>) é necessário!\
                \n Use '-h' para ajuda")
    selecionaAlgoritmos(args)


def selecionaAlgoritmos(args):
    grafo = Grafo(args['<arquivoDeGrafo>'])
    vertice = int(args['-v'] or 1)
    executaTodos = not(args['-l'] or args['-e'] or args['-d'])

    if args['-l'] or executaTodos:
        print("\nExecutando Busca em Largura a partir do vertice", vertice)
        Algoritmos.buscaEmLargura(grafo, vertice)
    if args['-e'] or executaTodos:
        print("\nBuscando Ciclo Euleriano")
        Algoritmos.algoritmoDeHierholzer(grafo)
    if args['-d'] or executaTodos:
        print("\nExecutando Djikstra a partir do vertice", vertice)
        Algoritmos.dijkstra(grafo, vertice)    
  

if __name__ == '__main__':
    args = docopt(__doc__)
    check_args(args)
