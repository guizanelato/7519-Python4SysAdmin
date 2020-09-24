
import pymongo
import flask 
import bson


app = flask.Flask(__name__)

client = pymongo.MongoClient()

collection = client.pessoa


#          FORMA   O QUE   ONDE
# endpoint http://dominio/endpoint

@app.route('/' , methods = ['GET'])
def hello_world():
    documento = {
        'data': 'Minha primeira API em flask'
    }

    return flask.jsonify(documento)

@app.route('/documents', methods = ['GET'])
def get_all_documents():
    documentos = [
                {
                   'id':  str(d.get('_id')),
                   'nome': d.get('nome'),
                   'idade': d.get('idade'),
                   'UF': d.get('UF')

                } for d in collection.pessoa.find() 

            ]
    return flask.jsonify(documentos)

@app.route('/documents/delete/<nome>', methods = ['DELETE'])
def delete_by_name(nome):
    collection.pessoa.delete_one({
            'nome' : str(nome)
        })

    return flask.jsonify({'message': 'registro removido com sucesso'})

@app.route('/documents/insert' , methods = ['POST'])
def insert_user():
    
    doc = flask.request.json

    collection.pessoa.insert(doc)

    return flask.jsonify({'mensagem': 'usuário cadastrado com sucesso'})

@app.route('/documents/update/<user_id>', methods = ['PUT' , 'PATCH'])
def update_user_by_id(user_id):
    user = {
            '_id': bson.ObjectId(user_id)

            }

    collection.pessoa.update(user, {
            '$set' : flask.request.json
        })

    user = collection.pessoa.find_one({
            '_id': bson.ObjectId(user_id)
        })

    return flask.jsonify({
            'id': str(user.get('_id')),
            'nome': user.get('nome'),
            'uf': user.get('UF'),
            'idade': user.get('idade')
        })



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

