
from flask import Flask, jsonify 
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/get_users', methods = ['GET'])
def get_users():
    try:
        client = MongoClient(host='200.100.50.17')
        collection = client.pessoa
    except Exception as err:
        print('Não foi possível conectar no banco de dados', err)
    
    else:
        documents = [
                {
                    'id': str(u.get('_id')),
                    'nome': u.get('nome'),
                    'idade': u.get('idade'),
                    'uf': u.get('uf')
                    
                } for u in collection.pessoa.find()  
                         
        ]

        return jsonify(documents) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)



