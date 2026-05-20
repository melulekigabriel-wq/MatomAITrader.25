def detect_order_block():

    return "Bullish Order Block"


def detect_fvg():

    return "Fair Value Gap Found"


def detect_liquidity_sweep(prices):

    if len(prices) < 5:
        return "NO LIQUIDITY SWEEP"

    # Possible bullish sweep
    if prices[-2] > prices[-3] and prices[-1] < prices[-2]:
        return "BUY-SIDE LIQUIDITY SWEEP"

    # Possible bearish sweep
    elif prices[-2] < prices[-3] and prices[-1] > prices[-2]:
        return "SELL-SIDE LIQUIDITY SWEEP"

    return "NO LIQUIDITY SWEEP"


def detect_equal_highs(prices):

    if abs(prices[-1] - prices[-2]) < 0.0005:
        return "EQUAL HIGHS DETECTED"

    return "NO EQUAL HIGHS"


def detect_equal_lows(prices):

    if abs(prices[-1] - prices[-2]) < 0.0005:
        return "EQUAL LOWS DETECTED"

    return "NO EQUAL LOWS"
