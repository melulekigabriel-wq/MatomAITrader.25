from datetime import datetime

def get_market_session():

    hour = datetime.utcnow().hour

    # UTC times
    if 0 <= hour < 7:
        return "ASIAN SESSION"

    elif 7 <= hour < 13:
        return "LONDON SESSION"

    elif 13 <= hour < 21:
        return "NEW YORK SESSION"

    return "MARKET CLOSED"


def get_volatility():

    hour = datetime.utcnow().hour

    if 7 <= hour <= 16:
        return "HIGH VOLATILITY"

    elif 0 <= hour < 7:
        return "LOW VOLATILITY"

    return "MODERATE VOLATILITY"
