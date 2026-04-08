from sqlalchemy.orm import Session
from app.models.registration import Registration

def get_all(db: Session):
    return db.query(Registration).all()

def get_by_id(db: Session, reg_id: int):
    return db.query(Registration).filter(Registration.id == reg_id).first()

def create(db: Session, data):
    reg = Registration(**data.dict())
    db.add(reg)
    db.commit()
    db.refresh(reg)
    return reg

def delete(db: Session, reg):
    db.delete(reg)
    db.commit()

def count_by_event(db: Session, event_id: int):
    return db.query(Registration).filter(Registration.event_id == event_id).count()

def get_by_user_event(db: Session, user_id: int, event_id: int):
    return db.query(Registration).filter(
        Registration.user_id == user_id,
        Registration.event_id == event_id
    ).first()