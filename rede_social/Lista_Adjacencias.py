class Grafo:
    
    def __init__(self,vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def adiciona_aresta(self, vertice_u,vertice_v):
        #adiciona na lista que está na posição
        self.grafo[vertice_u - 1].append(vertice_v)
        self.grafo[vertice_v - 1].append(vertice_u)

    def mostra_lista_posicao(self,posicao):
        print(self.grafo[posicao-1])
        #for i in self.grafo[posicao-1]:
        #    print(i)
    def mostra_lista(self):
        for i in range(self.vertices):
            print(f'{i+1}: {self.grafo[i]} ',end='   ')
g = Grafo(4)
g.adiciona_aresta(1,2)
g.adiciona_aresta(1,3)
g.adiciona_aresta(1,4)
g.mostra_lista()