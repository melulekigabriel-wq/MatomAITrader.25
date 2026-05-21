from signals import generate_signal
from database import Trade, SessionLocal

def run_engine():

    data = generate_signal()

    db = SessionLocal()

    trade = Trade(
        pair=data["pair"],
        signal=data["signal"],
        confidence=data["confidence"],
        entry=data["entry"],
        stop_loss=data["stop_loss"],
        take_profit=data["take_profit"],
        trend=data["trend"],
        session_name=data["session"]
    )

    db.add(trade)
    db.commit()
    db.close()

    return data
