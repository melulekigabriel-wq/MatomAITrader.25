import random
from candles import detect_candlestick_pattern
from database import Trade, SessionLocal
from market_structure import (
    detect_bos,
    detect_trend,
    detect_choch,
    detect_swing_high,
    detect_swing_low
)
from smc import (
    detect_order_block,
    detect_fvg,
    detect_liquidity_sweep,
    detect_equal_highs,
    detect_equal_lows
)
from session import get_market_session, get_volatility
from market_data import get_price
from timeframes import analyze_timeframes
from config import PAIRS

def calculate_confidence(bos, trend, overall_trend):

    confidence = 50

    if "BULLISH" in bos:
        confidence += 10

    if trend == overall_trend:
        confidence += 20

    confidence += random.randint(5, 15)

    return min(confidence, 95)

    if overall_trend == "BULLISH":
    confidence += 10

    confidence += random.randint(5, 10)

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

    choch = detect_choch(prices)

    swing_high = detect_swing_high(prices)

    swing_low = detect_swing_low(prices)

    timeframe_analysis, overall_trend = analyze_timeframes()

    order_block = detect_order_block()

    liquidity = detect_liquidity_sweep(prices)

    equal_highs = detect_equal_highs(prices)

    equal_lows = detect_equal_lows(prices)

    fvg = detect_fvg()

    session = get_market_session()

    volatility = get_volatility()

    candlestick = detect_candlestick_pattern()

    confidence = calculate_confidence(
        bos,
        trend,
        overall_trend
    )

    signal = "BUY"

    if overall_trend == "BEARISH":
        signal = "SELL"

    entry = round(live_price, 5)

    stop_loss = round(entry - 0.0020, 5)

    take_profit = round(entry + 0.0050, 5)

    db = SessionLocal()

    trade = Trade(
    pair=pair,
    signal=signal,
    confidence=confidence,
    entry=entry,
    stop_loss=stop_loss,
    take_profit=take_profit,
    trend=trend,
    session_name=session
    )

    db.add(trade)

    db.commit()

    db.close()

    return {
        "equal_highs": equal_highs,
        "equal_lows": equal_lows,
        "choch": choch,
        "swing_high": swing_high,
        "swing_low": swing_low,
        "session": session,
        "volatility": volatility,
        "candlestick": candlestick,
        "pair": pair,
        "signal": signal,
        "confidence": confidence,
        "bos": bos,
        "trend": trend,
        "overall_trend": overall_trend,
        "timeframes": timeframe_analysis,
        "order_block": order_block,
        "liquidity": liquidity,
        "fvg": fvg,
        "entry": entry,
        "stop_loss": stop_loss,
        "take_profit": take_profit
    }
