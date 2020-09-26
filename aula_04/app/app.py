
from flask import Flask,  jsonify, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def hello_from_container():

    payload = {
            'timestamp': str(datetime.now()),
            'message': 'Minha primeira aplicação em python dentro de um container'
            
            }

    return jsonify(payload)

@app.route('/index', methods = ['GET'])
def return_index():
    return render_template('index.html', context=None)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



