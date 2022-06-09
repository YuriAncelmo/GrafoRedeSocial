
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
            print(i)
            print(self.grafo[i])
        #MOstra tudo, porém em uma linha só
        #print(self.grafo.__str__())


g = Grafo(5)
g.mostra_matriz()
g.adiciona_aresta(1,2)
g.adiciona_aresta(1,3)
g.adiciona_aresta(1,4)
g.adiciona_aresta(2,5)
g.mostra_matriz()
