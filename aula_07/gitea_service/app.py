
from flask import Flask, redirect

from routes.gitea import blueprint as gitea

app = Flask(__name__)

app.register_blueprint(gitea)

@app.route('/', methods = ['GET'])
def get_docker():
    return redirect('/gitea')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

