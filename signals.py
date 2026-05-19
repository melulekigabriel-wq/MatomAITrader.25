import random
from market_structure import detect_bos, detect_trend
from smc import detect_order_block, detect_liquidity, detect_fvg

def generate_signal():

    prices = [100, 102, 104, 106]

    bos = detect_bos(prices)
    trend = detect_trend(prices)

    order_block = detect_order_block()
    liquidity = detect_liquidity()
    fvg = detect_fvg()

    signal = "BUY"
    confidence = random.randint(80, 95)

    return {
        "signal": signal,
        "confidence": confidence,
        "bos": bos,
        "trend": trend,
        "order_block": order_block,
        "liquidity": liquidity,
        "fvg": fvg
    }
