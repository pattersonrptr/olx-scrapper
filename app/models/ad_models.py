from datetime import datetime
from sqlalchemy import Column, Integer, String, Numeric, Text, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from app.database import Base

class Ad(Base):
    __tablename__ = 'ad'
    
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, index=True)
    title = Column(String)
    price = Column(Numeric(10, 2))
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
