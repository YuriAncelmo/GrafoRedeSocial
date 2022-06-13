from collections import defaultdict
class Grafo:

    def __init__(self):
        #dicionario padrão
        self.grafo = defaultdict(set)

    def adiciona_aresta(self, pessoa_a, pessoa_b):
        # adiciona na lista de adjacência
        self.grafo[pessoa_a].add(pessoa_b)
        self.grafo[pessoa_b].add(pessoa_a)

    def mostra_conexao_n1(self, pessoa):
        print(f'Vizinhos de {pessoa}: {self.grafo[pessoa]}')

    def mostra_conexao_n2(self,pessoa):
        conexao_n2 = list()
#Há possibilidade de diminuir para O(n) ?
        for conexao in self.grafo[pessoa]:
            for possivelconexao in self.grafo[conexao]:
                if possivelconexao not in self.grafo[pessoa] and possivelconexao != pessoa:
                    conexao_n2.append(possivelconexao)
        print(conexao_n2)


    def estado_atual(self):
        print(list(self.grafo.keys()))

    def mostra_lista(self):
        for pessoa in self.grafo.keys():
            print(f'{pessoa}: {self.grafo[pessoa]} ', end='   ')


g = Grafo()
g.adiciona_aresta("Ana", "Maria")
g.adiciona_aresta("Ana", "Joao")
g.adiciona_aresta("Ana", "Yoh")
g.adiciona_aresta("Yoh", "Manta")
#g.mostra_lista()
#g.mostra_vizinhos("Ana")
#g.mostra_vizinhos("Yoh")
#g.mostra_lista()
#g.estado_atual()
g.mostra_conexao_n2("Ana")