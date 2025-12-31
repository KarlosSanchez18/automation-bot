import requests
from config import BOT_TOKEN, CHAT_ID

TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"


def enviar_mensagem(texto: str):
    payload = {
        "chat_id": CHAT_ID,
        "text": texto
    }

    response = requests.post(TELEGRAM_API_URL, json=payload)
    return response.json()
