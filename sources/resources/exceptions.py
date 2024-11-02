from flask import jsonify
from werkzeug.exceptions import HTTPException

# Classe base para exceções personalizadas
class BaseError(HTTPException):
    code = 400  # Código de status padrão, pode ser alterado nas subclasses
    description = "A base para todas as exceções personalizadas"

    def __init__(self, description=None, code=None):
        super().__init__()
        if description:
            self.description = description
        if code:
            self.code = code

    def response(self):
        response = jsonify({
            "error": self.__class__.__name__,
            "message": self.description,
        })
        response.status_code = self.code
        return response

# Exceção para autenticação
class AuthenticationError(BaseError):
    code = 401
    description = "Não autorizado. Por favor, verifique suas credenciais."

# Exceção para erros internos do servidor
class InternalServerError(BaseError):
    code = 500
    description = "Erro interno do servidor. Tente novamente mais tarde."
