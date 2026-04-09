from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from datetime import datetime

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    quota = Column(Integer, nullable=False)
    started_at = Column(DateTime, nullable=False)
    ended_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)