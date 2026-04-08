from sqlalchemy.orm import Session
from app.models.event import Event

def get_all(db: Session):
    return db.query(Event).all()

def get_by_id(db: Session, event_id: int):
    return db.query(Event).filter(Event.id == event_id).first()

def create(db: Session, data):
    event = Event(**data.dict())
    db.add(event)
    db.commit()
    db.refresh(event)
    return event

def update(db: Session, event, data):
    for key, value in data.dict(exclude_unset=True).items():
        setattr(event, key, value)
    db.commit()
    db.refresh(event)
    return event

def delete(db: Session, event):
    db.delete(event)
    db.commit()