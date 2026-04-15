import csv
import os

def ultimo_precio(moneda):
    if os.path.exists("data/prices.csv"):
        with open("data/prices.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
        moneda_rows = [row for row in rows if row[1] == moneda]
        last_moneda = moneda_rows[-1]
        return float(last_moneda[2])
    
def escribir_precio(timestamp, data):
    
    os.makedirs("data", exist_ok=True)
    
    mode = "a" if os.path.exists("data/prices.csv") else "w"

    with open("data/prices.csv", mode, newline = "") as file:
        writer = csv.writer(file)
        if mode == "w":
            writer.writerow(["timestamp", "coin", "price_usd"])
        writer.writerow([timestamp, "Bitcoin", data['bitcoin']['usd']])
        writer.writerow([timestamp, "Ethereum", data['ethereum']['usd']])
        writer.writerow([timestamp, "Solana", data['solana']['usd']])


