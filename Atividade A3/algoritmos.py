from collections import deque
from grafo import Grafo


def edmondsKarp(grafo, verticeInicial=1, verticeFinal=-1):
    qtdVertices = grafo.qtdVertices()

    if verticeFinal == -1:
        verticeFinal = qtdVertices

    fluxo = 0
    F = [[0 for y in range(qtdVertices + 1)] for x in range(qtdVertices + 1)]

    while True:
        caminhoAumentante = [-1 for x in range(qtdVertices + 1)]
        caminhoAumentante[verticeInicial] = -2

        capacidadeResidual = [0 for x in range(qtdVertices + 1)]
        capacidadeResidual[verticeInicial] = 999999999

        filaIterativa = deque([verticeInicial])

        fluxoCaminho, caminhoAumentante = BFSpEdmondsKarp(grafo,
                                                          verticeInicial,
                                                          verticeFinal, F,
                                                          caminhoAumentante,
                                                          capacidadeResidual,
                                                          filaIterativa)
        if fluxoCaminho == 0:
            break

        fluxo = fluxo + fluxoCaminho
        verticeAtual = verticeFinal

        while verticeAtual != verticeInicial:
            vizinho = caminhoAumentante[verticeAtual]
            F[vizinho][verticeAtual] = F[vizinho][verticeAtual] + fluxoCaminho
            F[verticeAtual][vizinho] = F[verticeAtual][vizinho] - fluxoCaminho
            verticeAtual = vizinho
    print("Fluxo máximo de ", verticeInicial, " a ", verticeFinal, ": ",
          fluxo, sep='')
    return fluxo


def BFSpEdmondsKarp(grafo, verticeInicial, verticeFinal, F,
                    caminhoAumentante, capacidadeResidual, filaIterativa):
    while len(filaIterativa) > 0:
        verticeAtual = filaIterativa.popleft()
        for vizinho in grafo.vizinhos(verticeAtual):
            residual = grafo.peso(verticeAtual, vizinho) - \
                            F[verticeAtual][vizinho]

            if (residual > 0) and (caminhoAumentante[vizinho] == -1):
                caminhoAumentante[vizinho] = verticeAtual
                capacidadeResidual[vizinho] = min(
                                             capacidadeResidual[verticeAtual],
                                             residual)
                if vizinho is not verticeFinal:
                    filaIterativa.append(vizinho)
                else:
                    return capacidadeResidual[verticeFinal], caminhoAumentante
    return 0, caminhoAumentante


def printEdmondsKarp(listaNiveis):
    for key, value in listaNiveis.items():
        print(str(key) + ":", str(value)[1:-1])


def coloracao(grafo: Grafo):       # grafo não-dirigido e não-ponderado
    vertices = sorted(list(grafo.getVertices()), key=lambda x: len(grafo.vizinhos(x)), reverse=True)

    mapa_de_cores = {}
    cores_usadas = []

    for vertice in vertices:
        cores_disponiveis = [True] * len(vertices)
        for vizinho in grafo.vizinhos(vertice):
            if vizinho in mapa_de_cores:
                cor = mapa_de_cores[vizinho]
                cores_disponiveis[cor] = False

        for cor, disponivel in enumerate(cores_disponiveis):
            if disponivel:
                mapa_de_cores[vertice] = cor
                if cor not in cores_usadas:
                    cores_usadas.append(cor)
                break

    print("Número mínimo de cores:",len(cores_usadas))
    print("Mapeamento vértice-cor: ",mapa_de_cores)
    return mapa_de_cores

def listaTemItemNaOutraLista(lista1, lista2):
    for item in lista1:
        if item in lista2:
            return True
    return False


def montaVizinhoBipartido(grafo):
    dictTudo = {}
    for vertice in grafo.vertices.keys():
        dictTudo.update({vertice: list(grafo.vizinhos(vertice).keys())})
    return dictTudo



def hopcroftKarp(grafo):    # grafo bipartido, não-dirigido e não-ponderado
    verticesDeU = montaVizinhoBipartido(grafo)

    encontrado = {}
    for u in verticesDeU:
        for v in verticesDeU[u]:
            if v not in encontrado:
                encontrado[v] = u
                break

    while 1:
        preds = {}
        nEncontrado = []
        vizinhoAnteriorDeU = dict([(u,nEncontrado) for u in verticesDeU])
        for v in encontrado:
            del vizinhoAnteriorDeU[encontrado[v]]
        vizinhosRestantes = list(vizinhoAnteriorDeU)
        
        while vizinhosRestantes and not nEncontrado:
            novosVizinhos = {}
            for u in vizinhosRestantes:
                for v in verticesDeU[u]:
                    if v not in preds:
                        novosVizinhos.setdefault(v,[]).append(u)
            vizinhosRestantes = []
            for v in novosVizinhos:
                preds[v] = novosVizinhos[v]
                if v in encontrado:
                    vizinhosRestantes.append(encontrado[v])
                    vizinhoAnteriorDeU[encontrado[v]] = v
                else:
                    nEncontrado.append(v)

        if not nEncontrado:
            nProcurado = {}
            for u in verticesDeU:
                for v in verticesDeU[u]:
                    if v not in preds:
                        nProcurado[v] = None
            return (encontrado,len(encontrado))