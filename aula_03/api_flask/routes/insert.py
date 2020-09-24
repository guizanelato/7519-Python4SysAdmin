
from flask import Blueprint, jsonify, request
from pymongo import MongoClient

blueprint = Blueprint('insert', __name__)

@blueprint.route('/documents/insert' , methods = ['POST'])
def insert_user():
    client = MongoClient()
    collection = client.pessoa

    doc = request.json

    collection.pessoa.insert(doc)

    return jsonify({'mensagem': 'usuário cadastrado com sucesso'})
