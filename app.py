from flask import Flask, request, jsonify

from Principal import Grafo
import json

app = Flask(__name__)

rede = Grafo()

@app.get("/rede")
def get_rede():
    return jsonify(rede.estado_atual())

@app.post("/rede/pessoa")
def add_pessoa():
    if request.is_json:
        pessoa = request.get_json()
        rede.adiciona_pessoa(pessoa)
        return pessoa, 201
    return {"Erro":"A requisição precisa ser json"},415