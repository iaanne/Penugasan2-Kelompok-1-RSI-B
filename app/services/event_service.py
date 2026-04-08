from sqlalchemy.orm import Session
from app.repositories import event_repository

def get_events(db: Session):
    return event_repository.get_all(db)

def get_event(db: Session, event_id: int):
    event = event_repository.get_by_id(db, event_id)
    if not event:
        raise Exception("Event not found")
    return event

def create_event(db: Session, data):
    return event_repository.create(db, data)

def update_event(db: Session, event_id: int, data):
    event = event_repository.get_by_id(db, event_id)
    if not event:
        raise Exception("Event not found")
    return event_repository.update(db, event, data)

def delete_event(db: Session, event_id: int):
    event = event_repository.get_by_id(db, event_id)
    if not event:
        raise Exception("Event not found")
    event_repository.delete(db, event)