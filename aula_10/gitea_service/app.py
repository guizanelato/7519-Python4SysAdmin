
from flask import Flask, redirect, session

from flask_session import Session

from routes.gitea import blueprint as gitea
from services.decorators import login_required

app = Flask(__name__)
app.config.from_object('config')
Session(app)

app.register_blueprint(gitea)


if __name__ == '__main__':
    app.run(host='0.0.0.0')


