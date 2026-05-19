import random

def analyze_timeframes():

    trends = ["BULLISH", "BEARISH"]

    analysis = {
        "15m": random.choice(trends),
        "1H": random.choice(trends),
        "4H": random.choice(trends),
        "Daily": random.choice(trends)
    }

    bullish_count = list(analysis.values()).count("BULLISH")

    bearish_count = list(analysis.values()).count("BEARISH")

    overall = "SIDEWAYS"

    if bullish_count > bearish_count:
        overall = "BULLISH"

    elif bearish_count > bullish_count:
        overall = "BEARISH"

    return analysis, overall
