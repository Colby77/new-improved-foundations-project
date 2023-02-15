from sqlalchemy.orm import Session

import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int=0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + 'fakehashedpassword'
    new_user = models.User(email=user.email, username=user.username)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    new_user_auth = models.Auth(user_id=new_user.user_id, password=fake_hashed_password)
    db.add(new_user_auth)
    db.commit()
    db.refresh(new_user_auth)

    # print(dir(new_user))
    # print(new_user.user_id)

    return new_user


def get_characters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Character).offset(skip).limit(limit).all()


def create_character(db: Session, character: schemas.CharacterCreate, user_id: int):
    db_character = models.Character(**character.dict(), creator=user_id)
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character