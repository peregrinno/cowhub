from flask import Flask, jsonify, request
from flask_cors import CORS
from pydantic import ValidationError
from settings import api_settings
from sources.resources.views.api import api_router 
from sources.resources.exceptions import (
    AuthenticationError,
    BaseError,
    InternalServerError,
)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

app.config['TITLE'] = api_settings.TITLE
app.config['VERSION'] = api_settings.VERSION

# Configurar CORS
origins = api_settings.CORS_ORIGINS
CORS(app, resources={r"/api/*": {"origins": origins}}, supports_credentials=True)

# Incluir rotas (adaptando o router para Flask)
app.register_blueprint(api_router, url_prefix="/api/resources")

# Tratamento de exceções
@app.errorhandler(BaseError)
def handle_base_error(error):
    response = error.response()
    return jsonify(response), response.status_code

@app.errorhandler(401)
def handle_authentication_error(error):
    auth_error = AuthenticationError()
    return jsonify(auth_error.response()), auth_error.status_code

@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({"validation_errors": error.errors()}), 422

@app.errorhandler(500)
def handle_internal_server_error(error):
    server_error = InternalServerError()
    return jsonify(server_error.response()), server_error.status_code

# Iniciar o servidor
if __name__ == "__main__":
    app.run(
        host=api_settings.HOST,
        port=api_settings.PORT,
        debug=True if api_settings.LOG_LEVEL == "debug" else False
    )
