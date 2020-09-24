
import bson

from flask import Blueprint, jsonify, request
from pymongo import MongoClient 

blueprint = Blueprint('insert_by_id', __name__)

@blueprint.route('/documents/update/<user_id>', methods = ['PUT' , 'PATCH'])
def update_user_by_id(user_id):
    
    client = MongoClient()
    collection = client.pessoa


    user = {
            '_id': bson.ObjectId(user_id)

            }

    collection.pessoa.update(user, {
            '$set' : request.json
        })

    user = collection.pessoa.find_one({
            '_id': bson.ObjectId(user_id)
        })

    return jsonify({
            'id': str(user.get('_id')),
            'nome': user.get('nome'),
            'uf': user.get('UF'),
            'idade': user.get('idade')
        })


