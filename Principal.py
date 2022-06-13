import json
from collections import defaultdict

class Grafo:

    def __init__(self):
        #dicionario padrão
        self.grafo = {
            'Ana':['Maria','João','Carlos','Vinicius'],
            'Maria':['Ana','Vinicius'],
            'João':['Luiza'],
            'Carlos':['Ana'],
            'Vinicius':['Ana'],
            'Luiza':['João']
        }

    def toJson(self):
        return json.dumps(self,default=lambda o: o.__dict__)

    def adiciona_conexao(self, pessoa_a, pessoa_b):
        # adiciona na lista de adjacência
        self.grafo[pessoa_a].add(pessoa_b)
        self.grafo[pessoa_b].add(pessoa_a)

    def adiciona_pessoa(self, pessoa):
        # adiciona na lista de adjacência
        for conexao in pessoa.conexoes:
            self.adiciona_conexao(pessoa, conexao)

    def mostra_conexao_n1(self, pessoa):
        print(f'Vizinhos de {pessoa}: {self.grafo[pessoa]}')

    def mostra_conexao_n2(self,pessoa):
        conexao_n2 = list()
#Validar se com matriz de adjacência é possível diminuir a complexidade
        for conexao in self.grafo[pessoa]:
            for possivelconexao in self.grafo[conexao]:
                if possivelconexao not in self.grafo[pessoa] and possivelconexao != pessoa:
                    conexao_n2.append(possivelconexao)
        print(conexao_n2)


    def estado_atual(self):
        return list(self.grafo.keys())

    def mostra_lista(self):
        for pessoa in self.grafo.keys():
            print(f'{pessoa}: {self.grafo[pessoa]} ', end='   ')