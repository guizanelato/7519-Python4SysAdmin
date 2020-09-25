
from flask import Blueprint, jsonify, render_template
import pymongo


blueprint = Blueprint('get_documents', __name__) 

@blueprint.route('/documents', methods = ['GET'])
def get_all_documents():

    client = pymongo.MongoClient()
    collection = client.pessoa
    
    documentos = [
                {
                   'id':  str(d.get('_id')),
                   'nome': d.get('nome'),
                   'idade': d.get('idade'),
                   'UF': d.get('UF')

                } for d in collection.pessoa.find() 

            ]

    return render_template('index.html', context=documentos)
