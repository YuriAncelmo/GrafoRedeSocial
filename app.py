from flask import Flask, request, jsonify

from Principal import Rede
import json

app = Flask(__name__)

rede = Rede()


@app.get("/rede")
def get_rede():
    return jsonify(rede.estado_atual())


@app.get("/rede/pessoa/n1")
def get_rede_pessoa_n1(nome_pessoa: str):
    return rede.mostra_conexao_n1(nome_pessoa)


@app.get("/rede/pessoa/n2")
def get_rede_pessoa_n2(nome_pessoa: str):
    return rede.mostra_conexao_n2(nome_pessoa)


@app.post("/rede/pessoa")
def add_pessoa(pessoa: str, conexoes):
    if request.is_json:
        # pessoa = request.get_json()
        rede.adiciona_pessoa(pessoa, conexoes)
        return pessoa, 201
    return {"Erro": "A requisição precisa ser json"}, 415
