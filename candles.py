import random

def detect_candlestick_pattern():

    patterns = [
        "Bullish Engulfing",
        "Bearish Engulfing",
        "Bullish Pin Bar",
        "Bearish Pin Bar",
        "Doji Reversal",
        "Strong Rejection Candle"
    ]

    return random.choice(patterns)
