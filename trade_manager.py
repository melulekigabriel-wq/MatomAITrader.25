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
