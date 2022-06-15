import json


class Rede:

    def __init__(self):
        self.grafo = {
            'Ana': ['Maria', 'João', 'Carlos', 'Vinicius'],
            'Maria': ['Ana', 'Vinicius'],
            'Vinicius': ['Ana'],
            'Luiza': ['João'],
            'Carlos': ['Ana'],
            'João': ['Luiza']
        }

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def adiciona_conexao(self, pessoa_a, pessoa_b):
        # adiciona na lista de adjacência
        self.grafo[pessoa_a].add(pessoa_b)
        self.grafo[pessoa_b].add(pessoa_a)

    def adiciona_pessoa(self, nome, conexoes):
        # adiciona na lista de adjacência
        # precisa validar se já existes
        self.grafo[nome] = conexoes

    def pessoa_existe(self, nome):
        return nome in self.grafo

    def conexoes_existem(self, conexoes):
        for conexao in conexoes:
            if not self.pessoa_existe(conexao):
                return False
        return True

    def mostra_conexoes(self, pessoa, nivel):
        if nivel == "1":
            return self.grafo[pessoa]
        if nivel == "2":
            conexao_n2 = list()
            # Validar se com matriz de adjacência é possível diminuir a complexidade
            for conexao in self.grafo[pessoa]:
                for possivelconexao in self.grafo[conexao]:
                    if possivelconexao not in self.grafo[pessoa] and possivelconexao != pessoa:
                        conexao_n2.append(possivelconexao)
            return conexao_n2

    def estado_atual(self):
        return list(self.grafo.keys())

    def mostra_lista(self):
        for pessoa in self.grafo.keys():
            print(f'{pessoa}: {self.grafo[pessoa]} ', end='   ')
