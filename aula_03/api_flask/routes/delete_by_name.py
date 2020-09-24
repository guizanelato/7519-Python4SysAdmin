
from flask import Blueprint, jsonify
from pymongo import MongoClient


blueprint = Blueprint('delete_by_name', __name__) 

@blueprint.route('/documents/delete/<nome>', methods = ['DELETE'])
def delete_by_name(nome):
    client = MongoClient()
    collection = client.pessoa
    
    collection.pessoa.delete_one({
            'nome' : str(nome)
        })

    return jsonify({'message': 'registro removido com sucesso'})
