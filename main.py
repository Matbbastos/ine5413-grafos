from Grafo import Grafo
import Buscas
import pprint


grafo = Grafo("dolphins2.net")

distancias,antecessores = Buscas.dijkstra(grafo,1)
Hierholzer = Buscas.algoritmoDeHierholzer(grafo)
largura = Buscas.buscaEmLargura(grafo, 1)
