def detect_bos(prices):

    if len(prices) < 4:
        return "NO BOS"

    if prices[-1] > prices[-2] > prices[-3]:
        return "BULLISH BOS"

    elif prices[-1] < prices[-2] < prices[-3]:
        return "BEARISH BOS"

    return "NO BOS"


def detect_trend(prices):

    if prices[-1] > prices[0]:
        return "BULLISH"

    elif prices[-1] < prices[0]:
        return "BEARISH"

    return "SIDEWAYS"


def detect_choch(prices):

    if len(prices) < 5:
        return "NO CHoCH"

    # Bullish reversal
    if prices[-5] > prices[-4] > prices[-3] and prices[-2] < prices[-1]:
        return "BULLISH CHoCH"

    # Bearish reversal
    elif prices[-5] < prices[-4] < prices[-3] and prices[-2] > prices[-1]:
        return "BEARISH CHoCH"

    return "NO CHoCH"


def detect_swing_high(prices):

    return max(prices)


def detect_swing_low(prices):

    return min(prices)
