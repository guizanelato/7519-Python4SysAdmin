
import pymongo
import flask 

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

