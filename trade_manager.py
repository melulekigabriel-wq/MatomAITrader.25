from database import Trade, SessionLocal

def close_trade(trade_id, result, closed_price):

    db = SessionLocal()

    trade = db.query(Trade).filter(Trade.id == trade_id).first()

    if not trade:
        return "Trade not found"

    trade.result = result
    trade.closed_price = closed_price
    trade.is_closed = 1

    # PnL calculation
    if trade.signal == "BUY":
        trade.pnl = closed_price - trade.entry
    else:
        trade.pnl = trade.entry - closed_price

    db.commit()
    db.close()

    return "Trade updated"
