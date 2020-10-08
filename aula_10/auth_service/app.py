
import uuid

from flask import Flask, session
from flask_session import Session
from redis import Redis

from routes.auth import blueprint as auth

app = Flask(__name__)
SESSION_TYPE = 'redis'
SESSION_REDIS = Redis(host='200.100.50.90', port=6379, password='Redis2019!')

app.config.from_object(__name__)
Session(app)

app.secret_key =  str(uuid.uuid4())

app.register_blueprint(auth)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
