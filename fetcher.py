import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

url = os.getenv("COINGECKO_URL")


def consulta_api():
    response = requests.get(url)
    data = response.json()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return data, timestamp