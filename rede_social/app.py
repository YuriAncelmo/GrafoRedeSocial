import json

from flask import Flask, abort, request
from flask_restx import fields, Resource, Api, reqparse
from business import Rede

api = Api()
app = Flask(__name__)
api.init_app(app, version='1.0', title='API rede de conexões', description='API que simula uma rede de conexões')

ns_rede = api.namespace('rede', description='Operações na rede')
ns_conexaopessoa = api.namespace('rede/conexao/pessoa', description='Operações com a conexão de uma pessoa')
ns_pessoa = api.namespace('rede/pessoa', description='Operações com pessoa')


rede = Rede.Rede()


@ns_rede.route('/')
class Rede(Resource):
    """Lista o estado da rede atual"""
    @ns_rede.doc('Estado atual')
    @ns_conexaopessoa.response(200, 'Busca realizada com sucesso')
    @ns_conexaopessoa.response(400, 'Requisição invalida')
    def get(self):
        return rede.estado_atual()


conexoes_fields = api.model('conexoes', {
    'nome_pessoa':
        fields.String(required=True, help="Para ver a conexão é necessário informar uma pessoa"),
    'nivel':
        fields.String(required=True, help="Nível de conexão você espera que retorne 1 ou 2"),
})
pessoa_fields = api.model('Pessoa', {
    'nome': fields.String(readonly=False, required=True, description='Nome da pessoa'),
    'conexoes':
        fields.List(fields.String, readonly=False, required=False, description='Nome das pessoas que são suas conexões')
})


@ns_conexaopessoa.route('/')
class ConexaoPessoa(Resource):
    """Lista as conexões de uma pessoa, sendo nível 1 ou 2"""
    @ns_conexaopessoa.doc('Lista de conexões')
    @ns_conexaopessoa.response(200, 'Busca realizada com sucesso')
    @ns_conexaopessoa.response(400, 'Nivel inválido')
    @ns_conexaopessoa.response(404, 'Pessoa não existe na rede')
    @ns_conexaopessoa.param('nome_pessoa', 'Nome da pessoa')
    @ns_conexaopessoa.param('nivel', 'Nivel da conexão')
    def get(self):
        args = request.args
        nome_pessoa = args['nome_pessoa']
        nivel = args['nivel']
        if not rede.pessoa_existe(nome_pessoa):
            return {"Erro": 'Pessoa não existe na rede'}, 404
        if nivel not in ['1', '2']:
            return {"Erro": 'Nivel inválido'}, 400
        return rede.mostra_conexoes(nome_pessoa, nivel), 200


@ns_pessoa.route('/')
class Pessoa(Resource):
    @ns_pessoa.doc('Adicionar pessoa')
    @ns_pessoa.expect(pessoa_fields)
    @ns_pessoa.response(201, 'Pessoa criada')
    @ns_pessoa.response(400, 'Uma ou mais conexões especificadas não existem')
    @ns_pessoa.response(409, 'Pessoa já existe')
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nome')
        parser.add_argument('conexoes', action='append')
        args = parser.parse_args()
        nome = args['nome']
        conexoes = args['conexoes']
        if rede.pessoa_existe(nome):
            return {"Erro": 'Pessoa já existe'}, 409
        if not rede.conexoes_existem(conexoes):
            return {"Erro": 'Uma ou mais conexões especificadas não existem'}, 409
        rede.adiciona_pessoa(nome, conexoes)
        return {nome: rede.mostra_conexoes(nome, "1")}, 201


if __name__ == '__main__':
    app.run(debug=True)
