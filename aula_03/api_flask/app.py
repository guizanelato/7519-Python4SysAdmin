
import flask 

from routes.landing_page import blueprint as landing_page
from routes.get_documents import blueprint as get_documents
from routes.delete_by_name import blueprint as delete_by_name
from routes.insert import blueprint as insert
from routes.update_by_id import blueprint as update_by_id

## só entra parte de registro de blueprints

app = flask.Flask(__name__)

app.register_blueprint(landing_page)
app.register_blueprint(get_documents)
app.register_blueprint(delete_by_name)
app.register_blueprint(insert)
app.register_blueprint(update_by_id)

# https://http.cat/
@app.errorhandler(404)
def handler(err):
    return "Página não encontrada"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

