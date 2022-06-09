
class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        #Não entendi a inicialização
        self.grafo = [[0] * vertices for i in range(self.vertices)]

    def adiciona_aresta(self, vertice_u,vertice_v):
        #Por ser rede social , assumo que a conexão é bidirecional
        self.grafo[vertice_u-1][vertice_v-1] = 1
        self.grafo[vertice_v-1][vertice_u-1] = 1

    def mostra_matriz(self):
        print("A matriz de adjacências é")
        for i in range(self.vertices):
            #print(i)
            print(self.grafo[i])
        #MOstra tudo, porém em uma linha só
        #print(self.grafo.__str__())

v = int(input("Digite a quantidade de vertices: "))
g = Grafo(v)
a = int(input("Digite a quantidade de arestas: "))
for i in range(a):
    vertice_u = int(input("De onde parte o vertice?"))
    vertice_v = int(input("Para qual direção?"))
    g.adiciona_aresta(vertice_u, vertice_v)
g.mostra_matriz()
