import random
from market_structure import detect_bos, detect_trend
from smc import detect_order_block, detect_liquidity, detect_fvg
from market_data import get_price
from config import PAIRS

def calculate_confidence(bos, trend):

    confidence = 50

    if "BULLISH" in bos:
        confidence += 15

    if trend == "BULLISH":
        confidence += 15

    confidence += random.randint(5, 15)

    return min(confidence, 95)

def generate_signal():

    pair = random.choice(PAIRS)

    live_price = get_price(pair)

    if not live_price:
        live_price = 1.0850

    prices = [
        live_price - 0.0030,
        live_price - 0.0020,
        live_price - 0.0010,
        live_price
    ]

    bos = detect_bos(prices)

    trend = detect_trend(prices)

    order_block = detect_order_block()

    liquidity = detect_liquidity()

    fvg = detect_fvg()

    confidence = calculate_confidence(bos, trend)

    signal = "BUY"

    if trend == "BEARISH":
        signal = "SELL"

    entry = round(live_price, 5)

    stop_loss = round(entry - 0.0020, 5)

    take_profit = round(entry + 0.0050, 5)

    return {
        "pair": pair,
        "signal": signal,
        "confidence": confidence,
        "bos": bos,
        "trend": trend,
        "order_block": order_block,
        "liquidity": liquidity,
        "fvg": fvg,
        "entry": entry,
        "stop_loss": stop_loss,
        "take_profit": take_profit
    }
