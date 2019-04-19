from Grafo import Grafo
import Buscas
import pprint


grafo = Grafo("dolphins2.net")



distancias,antecessores = Buscas.dijkstra(grafo,1)

pprint.pprint(distancias)
pprint.pprint(antecessores)
for index in range(1,len(antecessores)):
    array = antecessores[index]
    print(index,": ",array,"; d=",distancias[index])

# temCiclo,vertices = Buscas.algoritmoDeHierholzer(grafo)
#
# if temCiclo:
#     print(1)
# else:
#     print(0)
#
# print(vertices)






