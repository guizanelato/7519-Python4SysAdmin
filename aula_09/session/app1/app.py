
import functools
import uuid

from flask import Flask, jsonify, session, redirect
from redis import Redis
from flask_session import Session


app = Flask(__name__)
SESSION_TYPE = 'redis'
SESSION_REDIS = Redis(host='200.100.50.90', port=6379, password='Redis2019!')

app.config.from_object(__name__)
Session(app)

app.secret_key =  'secret'


def login_required(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        if not session.get('auth'):
            return redirect('/sign-in')
        return function(*args, **kwargs)
    return wrapper


@app.route('/', methods = ['GET'])
def home():
    return jsonify({'message': 'você não está logado. efeture login em /sign-in'})

@app.route('/arealogada', methods = ['GET'])
@login_required
def area_logada():
        return jsonify({'app-secret_key': app.secret_key })

@app.route('/sign-in', methods=['GET'])
def sign_in():
    session['auth'] = True
    return redirect('http://example.com/service/gitea')


@app.route('/sign-out', methods=['GET'])
def sign_out():
    del session['auth']
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
