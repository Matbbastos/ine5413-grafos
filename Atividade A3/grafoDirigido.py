import copy


class GrafoDirigido:
    # vertices = { v1: {rotulo: "nome", v2:6,indexDasArestas:[5,6]},
    #              v2: {rotulo: "nome", v3:5, v1:6}}
    # arestas [ (v1, v2, 6) (v2, v3, 2)]

    def __init__(self, nomeDoArquivo=False, vertices={}, arestas=[]):
        self.vertices = vertices
        self.arestas = arestas
        if nomeDoArquivo:
            self.leArquivo(nomeDoArquivo)

    def getArestas(self):
        return self.arestas

    def getVertices(self):
        return self.vertices.keys()

    def qtdVertices(self):
        return len(self.vertices.keys())

    def qtdArestas(self):
        return len(self.arestas)

    def grau(self, vertice):
        return (len(self.vertices.get(vertice)) - 2)

    def getIndexDasArestasDoVertice(self, vertice):
        return self.vertices.get(vertice).get("indexDasArestas")

    def rotulo(self, vertice):
        return self.vertices.get(vertice).get("rotulo")

    def vizinhos(self, vertice):
        dicionarioVizinhosDoVertice = copy.copy(self.vertices.get(vertice))
        dicionarioVizinhosDoVertice.pop("rotulo")
        dicionarioVizinhosDoVertice.pop("indexDasArestas")
        return dicionarioVizinhosDoVertice

    def haAresta(self, vertice1, vertice2):
        return vertice2 in self.vertices.get(vertice1)

    def peso(self, vertice1, vertice2):
        return self.vertices.get(vertice1).get(vertice2, 999999999)

    def leArquivo(self, nomeArquivo):
        arquivo = open(nomeArquivo, "r")

        taNaParteDeEdges = False

        for linha in arquivo:
            if "vertice" in linha:
                continue

            if "edge" in linha or "arc" in linha:
                taNaParteDeEdges = linha
                continue

            if not taNaParteDeEdges:
                vertice, rotulo = linha.split()
                vertice = int(vertice)
                self.vertices.update(
                    {vertice: {"rotulo": rotulo, "indexDasArestas": []}})

            if taNaParteDeEdges:
                vertice, vizinho, peso = linha.split()
                vertice = int(vertice)
                vizinho = int(vizinho)
                peso = float(peso)

                size = len(self.arestas)

                indexesVertice = self.vertices.get(
                    vertice).get("indexDasArestas")
                indexesVertice.append(size)
                self.vertices.get(
                    vertice).update({vizinho: peso,
                                    "indexDasArestas": indexesVertice})

                self.arestas.append((vertice, vizinho, peso))

    def getGrafoTransposto(self):
        novoDicVertices = {}
        novaListaArestas = []
        for vertice in self.vertices.keys():
            novoDicVertices.update(
                    {vertice: {
                        "rotulo": self.vertices.get(vertice).get('rotulo'),
                        "indexDasArestas": []}})

        for vertice, vizinho, peso in self.arestas:
            size = len(novaListaArestas)
            indexesVizinho = novoDicVertices.get(
                            vizinho).get("indexDasArestas")
            indexesVizinho.append(size)
            novoDicVertices.get(
                vizinho).update({vertice: peso,
                                "indexDasArestas": indexesVizinho})
            novaListaArestas.append((vizinho, vertice, peso))
        return GrafoDirigido(vertices=novoDicVertices,
                             arestas=novaListaArestas)
