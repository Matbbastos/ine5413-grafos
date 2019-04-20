import pprint


def algoritmoDeHierholzer(grafo):
    qtdDeArestas = grafo.qtdArestas()
    arestasVisitadas = [False] * qtdDeArestas

    vertice = 1
    temCicloEuleriano, ciclo = buscaSubcicloEuleriano(grafo, vertice, arestasVisitadas)

    if not temCicloEuleriano or len(list(filter(lambda x: not x, arestasVisitadas))) > 0:
        existe, resultado = False, None
    else:
        existe, resultado = True, ciclo
    printaCiclo(existe, resultado)
    return existe, resultado


def printaCiclo(existe, resultado):
    if existe:
        print(1)
        print(str(resultado)[1:-1])
    else:
        print(0)


def buscaSubcicloEuleriano(grafo, vertice, foiVisitada):
    ciclo = [vertice]
    pontoFinal = vertice

    while True:
        indexDasArestasNaoVisitadasLigadasAoVertice = \
            list(filter(lambda i: not foiVisitada[i], grafo.getIndexDasArestasDoVertice(vertice)))

        if len(indexDasArestasNaoVisitadasLigadasAoVertice) == 0:
            return False, "nao tem indexes nao visitados ligados ao vertice"
        else:
            indexDeArestaNaoVisitada = indexDasArestasNaoVisitadasLigadasAoVertice.pop(0)

            foiVisitada[indexDeArestaNaoVisitada] = True

            aresta = grafo.arestas[indexDeArestaNaoVisitada]

            if aresta[0] == vertice:
                vertice = aresta[1]
            else:
                vertice = aresta[0]

            ciclo.append(vertice)

        if vertice == pontoFinal:
            # TEM CICLO EULERIANO, CARAI
            break

    while True:
        arestasNaoVisitadas = [i for i, x in enumerate(foiVisitada) if not x]

        verticesDoCicloComArestasNaoVisitadas = [
            vertice for vertice in ciclo if
            listaTemItemNaOutraLista(grafo.getIndexDasArestasDoVertice(vertice), arestasNaoVisitadas)
        ]

        if len(verticesDoCicloComArestasNaoVisitadas) == 0:
            break

        x = verticesDoCicloComArestasNaoVisitadas.pop(0)

        r, ciclo2 = buscaSubcicloEuleriano(grafo, x, foiVisitada)

        if not r:
            return False, "nao tem subciclo euleriano a partir do vertice "

        index = ciclo.index(x)
        ciclo.pop(index)
        ciclo[index:index] = ciclo2

    return True, ciclo


def listaTemItemNaOutraLista(lista1, lista2):
    for item in lista1:
        if item in lista2:
            return True
    return False


def buscaEmLargura(grafo, verticeInicial):
    qtdVertices = grafo.qtdVertices()
    foiVisitado = [False] * (qtdVertices + 1)  # lista de status (foi visitado?) de cada vértice
    distanciaDeS = [999999999] * (qtdVertices + 1)  # lista de distâncias de s a cada vértice
    antecessores = [None] * (qtdVertices + 1)  # lista de antecessores de cada vértice

    foiVisitado[verticeInicial] = True  # vértice inicial inicializa visitado
    distanciaDeS[verticeInicial] = 0  # distância até s = 0
    filaIterativa = [verticeInicial]  # enfila vértice s

    listaNiveis = {0: [verticeInicial]}

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

    printBuscaEmLargura(listaNiveis)


    # for nivel in listaNiveis:
    #     print(listaNiveis.get(nivel))

    return (distanciaDeS, antecessores)


def printBuscaEmLargura(listaNiveis):
    for key, value in listaNiveis.items():
        print(str(key) + ":", str(value)[1:-1])


def dijkstra(grafo, verticeInicial):
    qtdVertices = grafo.qtdVertices()
    distanciaDoInicial = [999999999.9] * (qtdVertices + 1)
    antecessores = [None] * (qtdVertices + 1)
    foiVisitado = [False] * (qtdVertices + 1)
    foiVisitado[0] = True

    distanciaDoInicial[verticeInicial] = 0

    while False in foiVisitado:
        verticesNaoVisitados = [index for index, verticeFoiVisitado in enumerate(foiVisitado) if not verticeFoiVisitado]
        distanciasNaoVisitadas = [distanciaDoInicial[i] for i in verticesNaoVisitados]


        menorDistancia = min(distanciasNaoVisitadas, default=None)
        menorIndice = verticesNaoVisitados[distanciasNaoVisitadas.index(menorDistancia)]

        if menorIndice is None:
            break

        verticeAtual = menorIndice

        foiVisitado[verticeAtual] = True

        vizinhosNaoVisitadosDoAtual = \
            {vizinho: peso for vizinho, peso in grafo.vizinhos(verticeAtual).items() if not foiVisitado[vizinho]}

        for vizinho, peso in vizinhosNaoVisitadosDoAtual.items():
            distanciaAtualizada = (float(distanciaDoInicial[verticeAtual]) + float(peso))
            if distanciaDoInicial[vizinho] > distanciaAtualizada:
                distanciaDoInicial[vizinho] = distanciaAtualizada
                if antecessores[verticeAtual] is None:
                    antecessores[verticeAtual] = []
                if antecessores[vizinho] is None:
                    antecessores[vizinho] = []
                antecessores[vizinho] = antecessores[verticeAtual] + [verticeAtual]

    antecessores[verticeInicial] = [verticeInicial]
    printDijkstra(distanciaDoInicial, antecessores)
    return distanciaDoInicial, antecessores


def printDijkstra(distancias, antecessores):
    for index in range(1,len(antecessores)):
        array = str(antecessores[index])[1:-1]
        print(str(index)+":",array+"; d="+str(distancias[index]))