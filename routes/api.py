from flask import Blueprint, request, jsonify
from bot.telegram_bot import enviar_mensagem

api_blueprint = Blueprint("api", __name__)


@api_blueprint.route("/enviar", methods=["POST"])
def enviar_para_telegram():
    dados = request.json

    if not dados or "mensagem" not in dados:
        return jsonify({"erro": "Mensagem não fornecida"}), 400

    resposta = enviar_mensagem(dados["mensagem"])
    return jsonify(resposta)
