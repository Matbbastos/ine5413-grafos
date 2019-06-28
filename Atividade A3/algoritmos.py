from collections import deque


def edmondsKarp(grafo, verticeInicial, verticeFinal, redeResidual):
    # grafo dirigido e ponderado
    qtdVertices = grafo.qtdVertices()
    foiVisitado = [False] * (qtdVertices + 1)
    antecessores = [None] * (qtdVertices + 1)

    foiVisitado[verticeInicial] = True
    filaIterativa = deque([verticeInicial])

    # listaNiveis = {0: [verticeInicial]}

    while len(filaIterativa) != 0:
        verticeAtual = filaIterativa.popleft()
        listaVizinhos = grafo.vizinhos(verticeAtual)
        for vizinho in listaVizinhos:
            if not foiVisitado[vizinho] and (c(arestaEmQuestao) - f(arestaEmQuestao > 0)):
                foiVisitado[vizinho] = True
                antecessores[vizinho] = verticeAtual

                # vizinhosDoNivel = listaNiveis.get(distanciaDoInicial[vizinho], [])
                # vizinhosDoNivel.append(vizinho)
                # listaNiveis.update({distanciaDoInicial[vizinho]: vizinhosDoNivel})

                if vizinho == verticeFinal:
                    p = (verticeFinal)
                    w = verticeFinal
                    while w != verticeInicial:
                        w = antecessores[w]
                        p = (w) uniao p
                    return p
                filaIterativa.append(vizinho)

    # printEdmondsKarp(listaNiveis)
    return null


def printEdmondsKarp(listaNiveis):
    for key, value in listaNiveis.items():
        print(str(key) + ":", str(value)[1:-1])


def hopcroftKarp(grafo):    # grafo bipartido, não-dirigido e não-ponderado
    pass


def coloracao(grafo):       # grafo não-dirigido e não-ponderado
    pass
