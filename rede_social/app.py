from flask import Flask, request
from flask_restx import fields, Resource, Api, reqparse
from business.Principal import Rede

api = Api()
app = Flask(__name__)
api.init_app(app, version='1.0', title='API rede de conexões', description='API que simula uma rede de conexões')

ns_rede = api.namespace('rede', description='Operações na rede')
ns_pessoa = api.namespace('rede/pessoa', description='Operações com pessoa')

model = api.model('Pessoa', {
    'nome': fields.String(readonly=False, required=True, description='Nome da pessoa'),
    'conexoes': fields.List(fields.String
                            , readonly=False
                            , required=False
                            , description='Nome das pessoas que são suas conexões')
})


class RedeDAO(object):

    def __init__(self):
        self.rede = Rede()

    def get(self):
        return self.rede


rDAO = RedeDAO()


class PessoaDAO(object):

    def __init__(self):
        self.rede = rDAO.rede

    def put(self, nome, conexoes):
        rede = rDAO.get()
        if rede.pessoa_existe(nome):
            return {'Erro', 'Pessoa já existe'}, 409
        for conexao in conexoes:
            if not rede.pessoa_existe(conexao):
                return {'Erro', f'A conexão {conexao} não existe'}, 400
        rede.adiciona_pessoa(nome, conexoes)
        return rede.mostra_conexao_n1(nome)


pDAO = PessoaDAO()


@ns_rede.route('/')
class Rede(Resource):
    """Lista o estado da rede atual"""
    @ns_rede.doc('estado_atual')
    def get(self):
        return rDAO.get().estado_atual()


@ns_pessoa.route('/')
class Pessoa(Resource):
    """Lista as conexões de uma pessoa, sendo nível 1 ou 2"""
    @ns_pessoa.doc('Lista de conexões')
    def get(self, nome_pessoa, nivel):
        if nivel == '1':
            return rDAO.get().mostra_conexao_n1(nome_pessoa)
        elif nivel == '2':
            return rDAO.get().mostra_conexao_n2(nome_pessoa)
        else:
            api.abort(404, 'Nivel inválido')

    @ns_pessoa.doc('Adicionar pessoa')
    @ns_pessoa.expect(model)
    # @ns_pessoa.marshal_with(model, code=201)
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nome')
        parser.add_argument('conexoes', action='append')
        args = parser.parse_args()
        nome = args['nome']
        conexoes = args['conexoes']
        return pDAO.put(nome, conexoes)


if __name__ == '__main__':
    app.run(debug=True)
