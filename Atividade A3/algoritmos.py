from collections import deque


def dfsVisit(grafo, vertice, foiVisitado, stack):
    if not foiVisitado[vertice]:
        foiVisitado[vertice] = True
        vizinhos = grafo.vizinhos(vertice).keys()
        for vizinho in vizinhos:
            dfsVisit(grafo, vizinho, foiVisitado, stack)
        stack.appendleft(vertice)


def assign(grafoReverso, vertice, raiz, foiDesignado, classes):
    if not foiDesignado[vertice]:
        classes[raiz].append(vertice)
        foiDesignado[vertice] = True
        vizinhos = grafoReverso.vizinhos(vertice).keys()
        for vizinho in vizinhos:
            assign(grafoReverso, vizinho, raiz, foiDesignado, classes)


def kosaraju(grafo):
    stack = deque([])
    qtdVertices = grafo.qtdVertices()
    foiVisitado = [False] * (qtdVertices + 1)
    foiDesignado = [False] * (qtdVertices + 1)

    classes = [[] for i in range(qtdVertices + 1)]

    grafoReverso = grafo.getGrafoTransposto()

    for index, vertice in enumerate(grafo.vertices.keys()):
        dfsVisit(grafo, vertice, foiVisitado, stack)

    for vertice in stack:
        assign(grafoReverso, vertice, vertice, foiDesignado, classes)

    printComponentesFortementeConexas(classes)
    return classes


def printComponentesFortementeConexas(classes):
    for classe in classes:
        if len(classe) > 0:
            listaClasse = []
            for index, vertice in enumerate(classe):
                listaClasse.append(vertice)
            print(str(listaClasse)[1:-1])


def ordenacaoTopologica(grafo):
    foiVisitado = [False] * (grafo.qtdVertices()+1)
    fila = deque([])

    for i in grafo.getVertices():
        if not foiVisitado[i]:
            ordenacaoTopologicaSub(grafo, i, foiVisitado, fila)

    for index, b in enumerate(fila):
        print(grafo.rotulo(b), end='')
        if index < len(fila) - 1:
            print(' -> ', end='')
    print()


def ordenacaoTopologicaSub(grafo, v, foiVisitado, fila):
    foiVisitado[v] = True

    for i in grafo.vizinhos(v):
        if not foiVisitado[i]:
            ordenacaoTopologicaSub(grafo, i, foiVisitado, fila)

    fila.appendleft(v)


def prim(grafo):
    verticeInicial = 1
    qtdVertices = grafo.qtdVertices()
    foiVisitado = [False] * (qtdVertices + 1)
    chaves = [999999999] * (qtdVertices + 1)
    antecessores = [None] * (qtdVertices + 1)

    chaves[verticeInicial] = 0
    queue = [0] + list(grafo.vertices.keys())

    while len(queue) != 1:
        chavesNaoVisitadas = [chaves[i] for i in queue]
        menorChave = min(chavesNaoVisitadas)
        indexMenorVertice = chavesNaoVisitadas.index(menorChave)
        menorVertice = queue.pop(indexMenorVertice)
        foiVisitado[menorVertice] = True

        for vizinho in grafo.vizinhos(menorVertice).keys():
            pesoAresta = grafo.peso(menorVertice, vizinho)
            if vizinho in queue and pesoAresta < chaves[vizinho]:
                antecessores[vizinho] = menorVertice
                chaves[vizinho] = pesoAresta

    printPrim(antecessores, chaves)
    return antecessores, chaves


def printPrim(antecessores, chaves):
    arestas = []
    total = 0
    for chave in chaves:
        if chave < 999999999:
            total += chave
    print(total)
    for index, v in enumerate(antecessores):
        if v is not None:
            arestas.append(', {}-{}'.format(index, v))
    frmArestas = ''
    for aresta in arestas:
        frmArestas += str(aresta)
    print(frmArestas[2:])
