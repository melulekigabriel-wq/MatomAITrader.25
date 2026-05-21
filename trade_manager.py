from database import Trade, SessionLocal

def update_trade_result(trade_id, result, profit=0):

    db = SessionLocal()

    trade = db.query(Trade).filter(
        Trade.id == trade_id
    ).first()

    if trade:

        trade.result = result
        trade.profit = profit

        db.commit()

    db.close()

def get_statistics():

    db = SessionLocal()

    trades = db.query(Trade).all()

    total = len(trades)

    wins = len([
        t for t in trades
        if t.result == "WIN"
    ])

    losses = len([
        t for t in trades
        if t.result == "LOSS"
    ])

    open_trades = len([
        t for t in trades
        if t.result == "OPEN"
    ])

    win_rate = 0

    if total > 0:
        win_rate = round(
            (wins / total) * 100,
            2
        )

    db.close()

    return {
        "total": total,
        "wins": wins,
        "losses": losses,
        "open": open_trades,
        "win_rate": win_rate
    }
