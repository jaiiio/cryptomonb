from fetcher import consulta_api
from storage import ultimo_precio, escribir_precio
from alerts import crypto_prices
from notifier import enviar_msje
import os
import schedule
import time
import logging


#Variable de entorno
UMBRAL = 2.0  # porcentaje

#Crear carpeta logs
os.makedirs("logs", exist_ok=True)

#Logs
logging.basicConfig (
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    handlers = [
        logging.FileHandler("logs/monitor.log"),
        logging.StreamHandler()
    ]
)


def monitorear():
    logging.info("Iniciando ciclo de monitoreo")
    data, timestamp = consulta_api()
 
 #Envio de precios actuales
    logging.info(f"BTC: {data['bitcoin']['usd']} | ETH: {data['ethereum']['usd']} | SOL: {data['solana']['usd']}")

    message = (
        f"Precios actuales:\n"
        f"ETH: {data['ethereum']['usd']:,.2f}\n"
        f"BTC: {data['bitcoin']['usd']:,.2f}\n"
        f"SOL: {data['solana']['usd']:,.2f}\n"
    )
    enviar_msje(message)

    precio_ant_btc = ultimo_precio("Bitcoin")
    if precio_ant_btc:
        alerta = crypto_prices(data['bitcoin']['usd'], precio_ant_btc, UMBRAL, "Bitcoin")
        if alerta:
            logging.warning(alerta)
            enviar_msje(alerta)

    precio_ant_eth = ultimo_precio("Ethereum")
    if precio_ant_eth:
        alerta = crypto_prices(data['ethereum']['usd'], precio_ant_eth, UMBRAL, "Ethereum")
        if alerta:
            logging.warning(alerta)
            enviar_msje(alerta)

    precio_ant_sol = ultimo_precio("Solana")
    if precio_ant_sol:
        alerta = crypto_prices(data['solana']['usd'], precio_ant_sol, UMBRAL, "Solana")
        if alerta:
            logging.warning(alerta)
            enviar_msje(alerta)

    escribir_precio(timestamp, data)

schedule.every(1).minutes.do(monitorear)

while True:
    schedule.run_pending()
    time.sleep(1)

# #Carga env
# load_dotenv()

# #Variables de entorno
# url = os.getenv("COINGECKO_URL")
# token = os.getenv("TELEGRAM_TOKEN")
# chat_id = os.getenv("TELEGRAM_CHAT_ID")


# #Funciones

# def monitorear ():
#     logging.info("Iniciando ciclo de monitoreo")
#     #Llamada a la API
#     logging.info("Consultando la API")
#     response = requests.get(url)
#     data = response.json()
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     #Crea carpeta
#     os.makedirs("data", exist_ok= True)


#     #Envio de precios actuales
#     logging.info(f"BTC: {data['bitcoin']['usd']} | ETH: {data['ethereum']['usd']} | SOL: {data['solana']['usd']}")

#     message = (
#         f"Precios actuales:\n"
#         f"ETH: {data['ethereum']['usd']:,.2f}\n"
#         f"BTC: {data['bitcoin']['usd']:,.2f}\n"
#         f"SOL: {data['solana']['usd']:,.2f}\n"
#     )
#     enviar_msje(message)


#     mode = "a" if os.path.exists("data/prices.csv") else "w"

#     #Condicion para read
#     if os.path.exists("data/prices.csv"):
#         with open("data/prices.csv", "r") as file:
#             reader = csv.reader(file)
#             rows = list(reader)
#         bitcoin_rows = [row for row in rows if row[1] == "Bitcoin"]
#         last_bitcoin = bitcoin_rows[-1]
#         last_price_btc = float(last_bitcoin[2])

#         ethereum_rows = [row for row in rows if row[1] == "Ethereum"]
#         last_eth = ethereum_rows[-1]
#         last_price_eth = float(last_eth[2])

#         solana_rows = [row for row in rows if row[1] == "Solana"]
#         last_solana = solana_rows[-1]
#         last_price_sol = float(last_solana[2])

#         cambio_btc = ((data['bitcoin']['usd'] - last_price_btc) / last_price_btc) * 100
#         cambio_eth = ((data['ethereum']['usd'] - last_price_eth) / last_price_eth) * 100
#         cambio_sol = ((data['solana']['usd'] - last_price_sol) / last_price_sol) * 100

#         if cambio_btc > UMBRAL: 
#             logging.warning(f"ALERTA detectada: Bitcoin cambió {cambio_btc:.2f}%")
#             enviar_msje(f"⚠️ ALERTA: Bitcoin subió {cambio_btc:.2f}%")
#         elif cambio_btc < -UMBRAL:
#             logging.warning(f"ALERTA detectada: Bitcoin cambió {cambio_btc:.2f}%")
#             enviar_msje(f"⚠️ ALERTA: Bitcoin bajó {cambio_btc:.2f}%")

#         if cambio_eth > UMBRAL: 
#             logging.warning(f"ALERTA detectada: Ethereum cambió {cambio_eth:.2f}%")
#             enviar_msje(f"⚠️ ALERTA: Ethereum subió {cambio_eth:.2f}%")
#         elif cambio_eth < -UMBRAL:
#             logging.warning(f"ALERTA detectada: Ethereum cambió {cambio_eth:.2f}%")
#             enviar_msje(f"⚠️ ALERTA: Ethereum bajó {cambio_eth:.2f}%")

#         if cambio_sol > UMBRAL: 
#             logging.warning(f"ALERTA detectada: Solana cambió {cambio_sol:.2f}%")
#             enviar_msje(f"⚠️ ALERTA: Solana subió {cambio_sol:.2f}%")
#         elif cambio_sol < -UMBRAL:
#             logging.warning(f"ALERTA detectada: Solana cambió {cambio_sol:.2f}%")
#             enviar_msje(f"⚠️ ALERTA: Solana bajó {cambio_sol:.2f}%")

        

#     with open("data/prices.csv", mode, newline="") as file:
#         writer = csv.writer(file)
#         if mode == "w":
#             writer.writerow(["timestamp", "coin", "price_usd"])
#         writer.writerow([timestamp, "Bitcoin", data['bitcoin']['usd']])
#         writer.writerow([timestamp, "Ethereum", data['ethereum']['usd']])
#         writer.writerow([timestamp, "Solana", data['solana']['usd']])


# schedule.every(1).minutes.do(monitorear)

# while True:
#     schedule.run_pending()
#     time.sleep(1)