from sqlalchemy import Column, Integer, String, TIMESTAMP, SmallInteger
from sqlalchemy.sql import func
from app.database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    quota = Column(SmallInteger)
    started_at = Column(TIMESTAMP)
    ended_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())
