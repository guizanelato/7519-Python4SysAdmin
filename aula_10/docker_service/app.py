
from flask import Flask, redirect

from routes.docker_ import blueprint as docker

app = Flask(__name__)

app.register_blueprint(docker)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

