def detect_bos(prices):

    if len(prices) < 3:
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
