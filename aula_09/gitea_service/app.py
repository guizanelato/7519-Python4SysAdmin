
from flask import Flask, redirect, session

from routes.gitea import blueprint as gitea
from services.decorators import login_required

from flask_session import Session


app = Flask(__name__)
app.config.from_object('config')
Session(app)

app.register_blueprint(gitea)

@app.route('/', methods = ['GET'])
@login_required
def get_docker():
    return redirect('/teste')

if __name__ == '__main__':
    app.run(host='0.0.0.0')


@app.route('/teste', methods = ['GET'])
def teste():
    return redirect('/gitea')
