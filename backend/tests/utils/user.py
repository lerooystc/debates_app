from db.repository.user import create_new_user
from schemas.user import UserCreate
from sqlalchemy.orm import Session


def create_random_user(db: Session):
    user = UserCreate(name="fugggggg", email="random@qweqw.com", password="dimesman23")
    user = create_new_user(user=user, db=db)
    return user
