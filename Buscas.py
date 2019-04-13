import pprint








def algoritmoDeHierholzer(grafo):
    qtdDeArestas = grafo.qtdArestas()
    arestasVisitadas = [False] * qtdDeArestas

    vertice = grafo.vertices.get(1)
    buscaSubcicloEuleriano(grafo,vertice,arestasVisitadas)


def temArestasNaoVisitada(arestasVisitadas, indexDasArestasLigadasAoVertice):
    for index in indexDasArestasLigadasAoVertice:
        if not arestasVisitadas[index]:
            return True

    return False

def buscaSubcicloEuleriano(grafo,vertice,arestasVisitadas):
    ciclo = [vertice]
    pontoFinal = vertice

    indexDasArestasNaoVisitadasLigadasAoVertice = []

    for index, aresta in enumerate(grafo.arestas()):
        if (aresta[0] == vertice or aresta[1] == vertice) and not arestasVisitadas[index]:
            indexDasArestasNaoVisitadasLigadasAoVertice.append(index)

    while True:

        if temArestasNaoVisitada(arestasVisitadas,indexDasArestasNaoVisitadasLigadasAoVertice):
            return (False,None)
        else:
            indexDeArestaNaoVisitada = indexDasArestasNaoVisitadasLigadasAoVertice.pop(0)

            arestasVisitadas[indexDeArestaNaoVisitada] = True

            aresta = grafo.arestas[indexDeArestaNaoVisitada]

            if aresta[0] == vertice:
                vertice = aresta[1]
            else:
                vertice = aresta[0]

            ciclo.append(vertice)

        if vertice == pontoFinal:
            #TEM CICLO EULERIANO, CARAI
            break


















def buscaEmLargura(grafo, verticeInicial):
    qtdVertices = grafo.qtdVertices()
    foiVisitado = [False] * (qtdVertices + 1)  # lista de status (foi visitado?) de cada vértice
    distanciaDeS = [999999999] * (qtdVertices + 1)  # lista de distâncias de s a cada vértice
    antecessores = [None] * (qtdVertices + 1)  # lista de antecessores de cada vértice

    foiVisitado[verticeInicial] = True  # vértice inicial inicializa visitado
    distanciaDeS[verticeInicial] = 0  # distância até s = 0
    filaIterativa = [verticeInicial]  # enfila vértice s

    listaNiveis = {}

    while len(filaIterativa) != 0:
        verticeAtual = filaIterativa.pop(0)
        listaVizinhos = grafo.vizinhos(verticeAtual)
        for vizinho, peso in listaVizinhos.items():
            if not foiVisitado[vizinho]:
                foiVisitado[vizinho] = True
                distanciaDeS[vizinho] = distanciaDeS[verticeAtual] + 1
                antecessores[vizinho] = verticeAtual
                filaIterativa.append(vizinho)

                vizinhosDoNivel = listaNiveis.get(distanciaDeS[vizinho], [])
                vizinhosDoNivel.append(vizinho)
                listaNiveis.update({distanciaDeS[vizinho]: vizinhosDoNivel})



    pprint.pprint(listaNiveis)

    # for nivel in listaNiveis:
    #     print(listaNiveis.get(nivel))

    return (distanciaDeS, antecessores)
