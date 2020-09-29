
from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def landing_page():
    try:
        response = requests.get('http://200.100.50.5/mongo_service/get_users')
        response.raise_for_status()
    except requests.exceptions.HTTPError  as err:
        print(err)
        return render_template('index.html', context=None)

    else:
        return render_template('index.html', context=response.json()) 

if __name__ == '__main__' :
    app.run(host='0.0.0.0' , debug='True')
