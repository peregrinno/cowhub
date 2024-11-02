from flask import Blueprint, jsonify

# Criação do Blueprint para as rotas de "hello world"
hello_world_router = Blueprint("hello_world", __name__)

@hello_world_router.route("/greet", methods=["GET"])
def greet():
    return jsonify({"message": "Hello, World!"})

@hello_world_router.route("/farewell", methods=["GET"])
def farewell():
    return jsonify({"message": "Goodbye, World!"})
