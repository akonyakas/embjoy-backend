from sqlalchemy import bindparam
from sqlalchemy.orm import Session
from src.models.user import User
from src.schema.user import UserCreate, UserOut
from src.core.security import *


def create_user_entry(db: Session, user: UserCreate):
    from src.core.security import get_password_hash
    db_user = User(
        username=user.username,
        hashed_password=get_password_hash(user.password),  # Hash the password
        role=user.role,
        days_pregnant=user.days_pregnant,
        num_of_pregnancies=user.num_of_pregnancies,
        num_of_failed_pregnancies=user.num_of_failed_pregnancies,
        first_time_pregnancy=user.first_time_pregnancy,
        prev_failed_pregnancies=user.prev_failed_pregnancies,
        med_conditions=user.med_conditions
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def delete_user(db: Session, user_id: int):
    db.query(User).filter(User.id == user_id).delete()
    db.commit()


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_all_users(db: Session):
    return db.query(User).all()