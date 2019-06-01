"""
Usage: main.py (<arquivoDeGrafo>) [options]
          main.py -h | --help

Options:
  -h --help     se não especificado, chamam-se todas as funções
  -c            executa algoritmo de componentes fortemente conexas
  -o            executa algoritmo de ordenação topológica
  -a            executa algoritmo de Prim para árvore geradora mínima
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
    executaTodos = not(args['-c'] or args['-o'] or args['-a'])

    if args['-c'] or executaTodos:
        print("\nExecutando Algoritmo de Componentes Fortemente Conexas")
        algoritmos.componentesFortementeConexas(grafo)
    if args['-o'] or executaTodos:
        print("\nExecutando Algoritmo de Ordenação Topológica")
        algoritmos.ordenacaoTopologica(grafoDirigido)
    if args['-a'] or executaTodos:
        print("\nExecutando Algoritmo de Árvore Geradora Mínima (Prim)")
        algoritmos.prim(grafo)


if __name__ == '__main__':
    args = docopt(__doc__)
    check_args(args)


g = Grafo("dolphins.net")
A = algoritmos.componentesFortementeConexas(g)
print(A)
