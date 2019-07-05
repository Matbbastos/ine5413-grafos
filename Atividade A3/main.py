"""
Usage: main.py (<arquivoDeGrafo>) [options]
          main.py -h | --help

Options:
  -h --help     se não especificado, chamam-se todas as funções (com vértices inicial 1 e final n)
  -s vertice    indica número do vértice inicial
  -t vertice    indica número do vértice final
  -f            executa algoritmo de Fluxo Máximo (Edmonds-Karp), do vértice inicial ao vértice final (usa -s e -t)
  -e            executa algoritmo de Emparelhamento Máximo (Hopcroft-Karp)
  -c            executa algoritmo de Coloração de Vértices
"""
import algoritmos
from grafo import Grafo
from grafoDirigido import GrafoDirigido
from docopt import docopt


def check_args(args):
    if (not ['<arquivoDeGrafo>']):
        exit("(<arquivoDeGrafo>) é necessário!\
                \n Use '-h' para ajuda")
    selecionaAlgoritmos(args)


def selecionaAlgoritmos(args):
    grafo = Grafo(args['<arquivoDeGrafo>'])
    grafoDirigido = GrafoDirigido(args['<arquivoDeGrafo>'])

    verticeInicial = int(args['-s'] or 1)
    verticeFinal = int(args['-t'] or -1)
    executaTodos = not(args['-f'] or args['-e'] or args['-c'])

    if args['-f'] or executaTodos:
        if verticeFinal == -1:
            print("\nExecutando Algoritmo de Fluxo Máximo (Edmonds-Karp) do" +
                  " vértice", verticeInicial, "até o vértice final")
        else:
            print("\nExecutando Algoritmo de Fluxo Máximo (Edmonds-Karp) do" +
                  " vértice", verticeInicial, "ao vértice", verticeFinal)
        algoritmos.edmondsKarp(grafo, verticeInicial, verticeFinal)

    if args['-e'] or executaTodos:
        print("\nExecutando Algoritmo de " +
              "Emparelhamento Máximo (Hopcroft-Karp)")
        grafoDirigido = GrafoDirigido(args['<arquivoDeGrafo>'], bipartido=True)
        algoritmos.hopcroftKarp(grafoDirigido)

    if args['-c'] or executaTodos:
        print("\nExecutando Algoritmo de Coloração de Vértices")
        algoritmos.coloracao(grafo)


if __name__ == '__main__':
    args = docopt(__doc__)
    check_args(args)
