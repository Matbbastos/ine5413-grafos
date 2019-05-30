def componentesFortementeConexas(grafo):
    (c, t, a, f) = buscaEmProfundidade(grafo)
    grafoTrans = grafo.getGrafoTransposto()

    (cT, tT, aT, fT) = buscaEmProfundidade(grafoTrans, f)
    return aT


def buscaEmProfundidade(grafo, fDecrescente=False):
    qtdVertices = grafo.qtdVertices()

    foiVisitado = [False] * (qtdVertices + 1)
    tempoAteVisita = [999999999] * (qtdVertices + 1)
    tempoAposExploracao = [999999999] * (qtdVertices + 1)
    # antecessores = [[] for i in range(qtdVertices + 1)]
    antecessores = []

    tempo = 0
    if not fDecrescente:
        for vertice in grafo.vertices.keys():
            if not foiVisitado[vertice]:
                visitaEmProfundidade(grafo, vertice, foiVisitado, tempoAteVisita,
                                     antecessores, tempoAposExploracao, tempo)
    else:
        fDecrescente[0] *= -1
        for v in range(1, len(fDecrescente)):
            vertice = fDecrescente.index(max(fDecrescente))
            fDecrescente.pop(vertice)
            if not foiVisitado[vertice]:
                antecessores.append(
                    visitaEmProfundidade(grafo, vertice, foiVisitado, tempoAteVisita,
                                         [], tempoAposExploracao, tempo))

    return (foiVisitado, tempoAteVisita, antecessores, tempoAposExploracao)


def visitaEmProfundidade(grafo, vertice, foiVisitado, tempoAteVisita,
                         antecessores, tempoAposExploracao, tempo):
    foiVisitado[vertice] = True
    tempo += 1
    tempoAteVisita[vertice] = tempo

    for vizinho in grafo.vizinhos(vertice):
        if not foiVisitado[vizinho]:
            antecessores.append(vertice)
            print(antecessores)
            visitaEmProfundidade(grafo, vizinho, foiVisitado, tempoAteVisita,
                                 antecessores, tempoAposExploracao, tempo)
    tempo += 1
    tempoAposExploracao[vertice] = tempo
    return antecessores


def ordenacaoTopologica(grafo):
    pass


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
