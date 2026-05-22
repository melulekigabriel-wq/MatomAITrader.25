import os
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Trade(Base):

    __tablename__ = "trades"

    id = Column(Integer, primary_key=True)

    pair = Column(String)

    signal = Column(String)

    confidence = Column(Integer)

    entry = Column(Float)

    stop_loss = Column(Float)

    take_profit = Column(Float)

    trend = Column(String)

    session_name = Column(String)

    result = Column(String, default="OPEN")

    profit = Column(Float, default=0.0)

    # WIN RATE TRACKING FIELDS
    pnl = Column(Float, default=0.0)

    closed_price = Column(Float, default=0.0)

    is_closed = Column(Integer, default=0)

# Use PostgreSQL for Render, SQLite for local development
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///trades.db")

# Handle SQLite vs PostgreSQL driver differences
if DATABASE_URL.startswith("postgresql"):
    # Render uses postgresql+psycopg2
    if not DATABASE_URL.startswith("postgresql+psycopg2"):
        DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg2://")

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
