from db.repository.debate import create_new_debate
from schemas.debate import CreateDebate
from sqlalchemy.orm import Session
from tests.utils.user import create_random_user


def create_random_debate(db: Session):
    debate = CreateDebate(name="Bats vs. Knives", is_private=False)
    user = create_random_user(db=db)
    debate = create_new_debate(debate=debate, db=db, created_by=user.id)
    return debate
