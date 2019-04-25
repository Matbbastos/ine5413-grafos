from collections import deque

def buscaEmLargura(grafo, verticeInicial):
    qtdVertices = grafo.qtdVertices()
    foiVisitado = [False] * (qtdVertices + 1)
    distanciaDoInicial = [999999999] * (qtdVertices + 1)
    antecessores = [None] * (qtdVertices + 1)

    foiVisitado[verticeInicial] = True
    distanciaDoInicial[verticeInicial] = 0
    filaIterativa = deque([verticeInicial])

    listaNiveis = {0: [verticeInicial]}

    while len(filaIterativa) != 0:
        verticeAtual = filaIterativa.popleft()
        listaVizinhos = grafo.vizinhos(verticeAtual)
        for vizinho in listaVizinhos:
            if not foiVisitado[vizinho]:
                foiVisitado[vizinho] = True
                distanciaDoInicial[vizinho] = distanciaDoInicial[verticeAtual] + 1
                antecessores[vizinho] = verticeAtual
                filaIterativa.append(vizinho)

                vizinhosDoNivel = listaNiveis.get(distanciaDoInicial[vizinho], [])
                vizinhosDoNivel.append(vizinho)
                listaNiveis.update({distanciaDoInicial[vizinho]: vizinhosDoNivel})

    printBuscaEmLargura(listaNiveis)

    return (distanciaDoInicial, antecessores)

def printBuscaEmLargura(listaNiveis):
    for key, value in listaNiveis.items():
        print(str(key) + ":", str(value)[1:-1])

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

def buscaSubcicloEuleriano(grafo, vertice, foiVisitada):
    ciclo = [vertice]
    pontoFinal = vertice

    while True:
        indexDasArestasNaoVisitadasLigadasAoVertice = \
            deque(list(filter(lambda i: not foiVisitada[i], grafo.getIndexDasArestasDoVertice(vertice))))

        if len(indexDasArestasNaoVisitadasLigadasAoVertice) == 0:
            return False, "nao tem indexes nao visitados ligados ao vertice"
        else:
            indexDeArestaNaoVisitada = indexDasArestasNaoVisitadasLigadasAoVertice.popleft()

            foiVisitada[indexDeArestaNaoVisitada] = True

            aresta = grafo.arestas[indexDeArestaNaoVisitada]

            if aresta[0] == vertice:
                vertice = aresta[1]
            else:
                vertice = aresta[0]

            ciclo.append(vertice)

        if vertice == pontoFinal:
            break

    while True:
        arestasNaoVisitadas = [i for i, x in enumerate(foiVisitada) if not x]

        verticesDoCicloComArestasNaoVisitadas = deque([
            vertice for vertice in ciclo if
            listaTemItemNaOutraLista(grafo.getIndexDasArestasDoVertice(vertice), arestasNaoVisitadas)
        ])

        if len(verticesDoCicloComArestasNaoVisitadas) == 0:
            break

        x = verticesDoCicloComArestasNaoVisitadas.popleft()

        r, ciclo2 = buscaSubcicloEuleriano(grafo, x, foiVisitada)

        if not r:
            return False, "nao ha subciclo euleriano a partir do vertice "

        index = ciclo.index(x)
        ciclo.pop(index)
        ciclo[index:index] = ciclo2

    return True, ciclo

def printaCiclo(existe, resultado):
    if existe:
        print(1)
        print(str(resultado)[1:-1])
    else:
        print(0)

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

def floydWarshall(grafo):
	distanciasAnteriores = [][]
	distancias = [][]
	for arestas in grafo.arestas:
		distanciasAnteriores[aresta[0]][arestas[1]] = arestas[2]
		
	for k in range(grafo.qtdVertices()):
		for linha in distanciasAnteriores[0]:
			for coluna in distanciasAnteriores[1]:
				distancias[linha][coluna] = min(distanciasAnteriores[linha][coluna], distanciasAnteriores[linha][k]+ distanciasAnteriores[k][coluna]) 
		distanciasAnteriores = distancias
		
	printFloydWarshal(distancias)
	return distancias
		
def printFloydWarshal(distancias):
	contaLinhas = 1
	for linha in distancias:
		print(contaLinhas, str(linha)[1:-1])
		contaLinhas += 1
						
def listaTemItemNaOutraLista(lista1, lista2):
    for item in lista1:
        if item in lista2:
            return True
    return False