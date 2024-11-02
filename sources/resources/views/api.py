from flask import Blueprint
from .hello_word import hello_world_router

# Criação do Blueprint principal que agrupa as rotas com o prefixo
api_router = Blueprint("api", __name__)

# Registrando o Blueprint de hello world com o prefixo "/hello"
api_router.register_blueprint(hello_world_router, url_prefix="/hello")
