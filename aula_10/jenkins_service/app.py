
from flask import Flask, redirect

from routes.jenkins_ import blueprint as jenkins

app = Flask(__name__)

app.register_blueprint(jenkins)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

