import requests
import os
from datetime import datetime, timedelta

TWELVEDATA_API_KEY = os.getenv("TWELVEDATA_API_KEY", "demo")

def get_price(symbol="EUR/USD"):
    """Get current price for a symbol"""
    try:
        symbol_clean = symbol.replace("/", "")
        url = f"https://api.twelvedata.com/price?symbol={symbol_clean}&apikey={TWELVEDATA_API_KEY}"
        response = requests.get(url, timeout=5)
        data = response.json()
        
        if "price" in data:
            return float(data["price"])
        return None
    except Exception as e:
        print(f"❌ Error getting price: {str(e)}")
        return None

def get_ohlc_data(symbol="EUR/USD", interval="15min"):
    """Get OHLC data for technical analysis"""
    try:
        symbol_clean = symbol.replace("/", "")
        url = f"https://api.twelvedata.com/time_series?symbol={symbol_clean}&interval={interval}&apikey={TWELVEDATA_API_KEY}"
        response = requests.get(url, timeout=5)
        data = response.json()
        
        if "values" in data and len(data["values"]) > 0:
            latest = data["values"][0]
            return {
                "open": float(latest.get("open", 0)),
                "high": float(latest.get("high", 0)),
                "low": float(latest.get("low", 0)),
                "close": float(latest.get("close", 0)),
                "volume": latest.get("volume", 0)
            }
        return None
    except Exception as e:
        print(f"❌ Error getting OHLC data: {str(e)}")
        return None

def get_multiple_prices(symbols):
    """Get prices for multiple symbols at once"""
    prices = {}
    for symbol in symbols:
        price = get_price(symbol)
        prices[symbol] = price
    return prices

def get_intraday_data(symbol="EUR/USD"):
    """Get intraday market data"""
    try:
        symbol_clean = symbol.replace("/", "")
        url = f"https://api.twelvedata.com/time_series?symbol={symbol_clean}&interval=1min&apikey={TWELVEDATA_API_KEY}"
        response = requests.get(url, timeout=5)
        return response.json()
    except Exception as e:
        print(f"❌ Error getting intraday data: {str(e)}")
        return None
