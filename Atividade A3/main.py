"""
Usage: main.py (<arquivoDeGrafo>) [options]
          main.py -h | --help

Options:
  -h --help     se não especificado, chamam-se todas as funções
  -f            executa algoritmo de Fluxo Máximo (Edmonds-Karp)
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
    executaTodos = not(args['-f'] or args['-e'] or args['-c'])

    if args['-f'] or executaTodos:
        print("\nExecutando Algoritmo de Fluxo Máximo (Edmonds-Karp)")
        algoritmos.edmondsKarp(grafo)
    if args['-e'] or executaTodos:
        print("\nExecutando Algoritmo de Emparelhamento Máximo (Hopcroft-Karp)")
        algoritmos.hopcroftKarp(grafoDirigido)
    if args['-c'] or executaTodos:
        print("\nExecutando Algoritmo de Coloração de Vértices")
        algoritmos.coloracao(grafo)


if __name__ == '__main__':
    args = docopt(__doc__)
    check_args(args)
