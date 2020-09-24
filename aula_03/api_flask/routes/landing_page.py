
from flask import Blueprint, jsonify

blueprint = Blueprint('landing_page', __name__) 

@blueprint.route('/', methods = ['GET'])
def hello_world():
    documento = {
        'data': 'Minha primeira API em flask'
    }

    return jsonify(documento)
