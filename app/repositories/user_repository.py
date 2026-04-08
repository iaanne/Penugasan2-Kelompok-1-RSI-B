from sqlalchemy.orm import Session
from app.models.user import User

def get_all(db: Session):
    return db.query(User).all()

def get_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create(db: Session, data):
    user = User(**data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update(db: Session, user, data):
    for key, value in data.dict(exclude_unset=True).items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

def delete(db: Session, user):
    db.delete(user)
    db.commit()