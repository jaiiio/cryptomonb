import requests
import os
from dotenv import load_dotenv

#Carga de dotenv
load_dotenv()

#Carga variables de Fx
token = os.getenv("TELEGRAM_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

#Fx que envia post a telegram
def enviar_msje(mensaje):
    requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data = {"chat_id": chat_id, "text": mensaje}
    )
