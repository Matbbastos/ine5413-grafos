import random

def vizinhos(V, E, u):
    Nu = []
    for i in E:
        if i.count(u) == 1:
            iCopy = i.copy()
            iCopy.remove(u)    
            Nu.append(iCopy[0])
    return Nu

def grafoAleatorio(n, m):
    V = [i + 1 for i in range(random.randint(1, n))]
    indexAleatorio = random.shuffle(V)
    for indexAleatorio in V:
        # percorrer vértices aleatoriamente e adicionar ou não aresta
    
        
def buscaEmLargura (V, E, s):           # culpa do Valin: lista iniciada em index[1]
    indexS = s                          # índice do vértice s
    Cv = [False] * (len(V) + 1)         # lista de status (foi visitado?) de cada vértice
    Dv = [999999999] * (len(V) + 1)     # lista de distâncias de s a cada vértice
    Av = [None] * (len(V) + 1)          # lista de antecessores de cada vértice
    Nu = []                             # lista de vizinhos do vértice u
    Q = []                              # fila de iteração do algoritmo
    Cv[indexS] = True                   # vértice inicial inicializa visitado
    Dv[indexS] = 0                      # distância até s = 0
    Q.append(s)                         # enfila vértice s

    while len(Q) != 0:
        u = Q.pop()
        Nu = vizinhos(V, E, u)
        for i in Nu:
            if Cv[i] == False:
                Cv[i] = True
                Dv[i] = Dv[u] + 1
                Av[i] = u
                Q.append(i)
    print ("Vértices:", V, "\nDistâncias:", Dv[1:], "\nAntecessores:", Av[1:])
    return (Dv, Av)
        

V = [1,2,3,4,5]
E = [[1,2],[2,3],[2,4],[4,5]]
s = 1



buscaEmLargura(V, E, 1)
#vizinhos(V, E, 5)
