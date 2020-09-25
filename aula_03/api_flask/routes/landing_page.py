
from random import randint

from flask import Blueprint, jsonify, render_template

blueprint = Blueprint('landing_page', __name__) 

@blueprint.route('/', methods = ['GET'])
def hello_world():
    
    context = {
        'numeros': [ randint(0,9) for x in range(5) ]
    }

    return render_template('index.html', context=context) 
