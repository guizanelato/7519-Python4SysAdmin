
import flask 

app = flask.Flask(__name__)

#          FORMA   O QUE   ONDE
# endpoint http://dominio/endpoint

@app.route('/' , methods = ['GET'])
def hello_world():
    documento = {
        'data': 'Minha primeira API em flask'
    }

    return flask.jsonify(documento)

if __name__ == '__main__':
    app.run(host='0.0.0.0.0', port=5000)

