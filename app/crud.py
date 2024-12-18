from sqlalchemy.orm import Session
from model import Users
from schemas import UsersSchema


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Users).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(Users).filter(Users.id == user_id).first()


def create_user(db: Session, user: UsersSchema):
    _user = Users(name=user.name, email=user.email)
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user


def remove_user(db: Session, user_id: int):
    _user = get_user_by_id(db=db, user_id=user_id)
    db.delete(_user)
    db.commit()


def update_user(db: Session, user_id: int, name: str, email: str):
    _user = get_user_by_id(db=db, user_id=user_id)

    _user.name = name
    _user.email = email

    db.commit()
    db.refresh(_user)
    return _user