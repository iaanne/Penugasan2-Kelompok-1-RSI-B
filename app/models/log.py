import enum
from sqlalchemy import Column, Integer, String, TIMESTAMP, Enum, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class ActionEnum(str, enum.Enum):
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"

class EntityEnum(str, enum.Enum):
    USER = "USER"
    ACCOUNT = "ACCOUNT"
    ROLE = "ROLE"
    EVENT = "EVENT"
    REGISTRATION = "REGISTRATION"

class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    created_at = Column(TIMESTAMP, server_default=func.now())
    action = Column(Enum(ActionEnum))
    ip_address = Column(String)
    user_agent = Column(String)
    entity = Column(Enum(EntityEnum))
    entity_id = Column(Integer, nullable=True)
