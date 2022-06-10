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

        naoconexao = list()
        conexaodaconexao = list()
        # problema 1 - Considera a rede inteira
        for i in self.grafo.keys():
            if(i != pessoa):
                if i not in self.grafo[pessoa] and i not in naoconexao:
                    #para adicionar todos que não são minha conexao
                    naoconexao.append(i)
                else:#adiciona os vizinhos do meu vizinho
                    for c in self.grafo[i]:
                        if c not in conexaodaconexao and c != pessoa:
                            conexaodaconexao.append(c)
        #Para depois validar se dentro das minhas desconexões, há algum vizinho do meu vizinho.
        conexao_n2 = list()
        for n in naoconexao:
            if n in conexaodaconexao:
                conexao_n2.append(n)
        print(conexao_n2)
        #Talvez seja uma alternativa, primeiro ver os vizinhos do meus vizinhos, e depois validar se eles estão dentro da minha vizinhança


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