import requests
import os

API_KEY = os.getenv("MARKET_API_KEY")

def get_price(symbol="EUR/USD"):

    symbol = symbol.replace("/", "")

    url = f"https://api.twelvedata.com/price?symbol={symbol}&apikey={API_KEY}"

    response = requests.get(url)

    data = response.json()

    if "price" in data:
        return float(data["price"])

    return None
