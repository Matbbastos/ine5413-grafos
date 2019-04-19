import pprint
import copy
class Grafo:
    # vertices = { v1: {rotulo: "nome", v2:6,indexDasArestas:[5,6]}, v2: {rotulo: "nome", v3:5, v1:6}}
    # arestas [ (v1, v2, 6) (v2, v3, 2)]

    def __init__(self, nomeDoArquivo):
        self.vertices = {}
        self.arestas = []
        self.leArquivo(nomeDoArquivo)

    def getArestas(self):
        return self.arestas

    def qtdVertices(self):
        return len(self.vertices.keys())

    def qtdArestas(self):
        return len(self.arestas)

    def grau(self, vertice):
        return len(self.vertices.get(vertice))

    def getIndexDasArestasDoVertice(self,vertice):
        return self.vertices.get(vertice).get("indexDasArestas")

    def rotulo(self, vertice):
        return self.vertices.get(vertice).rotulo

    def vizinhos(self, vertice):
        huehue = copy.copy(self.vertices.get(vertice))
        huehue.pop("rotulo")
        huehue.pop("indexDasArestas")
        return huehue

    def haAresta(self, vertice1, vertice2):
        return vertice2 in self.vertices.get(vertice1)

    def peso(self, vertice1, vertice2):
        return self.vertices.get(vertice1).get(vertice2)

    def leArquivo(self, nomeArquivo):
        arquivo = open(nomeArquivo, "r")

        taNaParteDeEdges = False

        for linha in arquivo:
            if "vertice" in linha:
                continue

            if "edge" in linha:
                taNaParteDeEdges = True
                continue

            if not taNaParteDeEdges:
                vertice, rotulo = linha.split()
                vertice = int(vertice)
                self.vertices.update({vertice: {"rotulo": rotulo,"indexDasArestas":[]}})

            if taNaParteDeEdges:
                vertice, vizinho, peso = linha.split()
                vertice = int(vertice)
                vizinho = int(vizinho)
                peso = float(peso)

                size = len(self.arestas)

                indexesVizinho = self.vertices.get(vizinho).get("indexDasArestas")
                indexesVizinho.append(size)
                self.vertices.get(vizinho).update({vertice: peso,"indexDasArestas": indexesVizinho})

                indexesVertice = self.vertices.get(vertice).get("indexDasArestas")
                indexesVertice.append(size)
                self.vertices.get(vertice).update({vizinho: peso,"indexDasArestas": indexesVertice})

                self.arestas.append((vertice, vizinho, peso))
