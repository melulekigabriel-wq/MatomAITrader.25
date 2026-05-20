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

DATABASE_URL = "sqlite:///trades.db"

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
