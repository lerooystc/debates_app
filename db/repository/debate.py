from sqlalchemy.orm import Session
from schemas.debate import DebateCreate
from db.models.debate import Debate


def create_new_debate(debate: DebateCreate, db: Session):
    debate = Debate(
        **debate.model_dump(),
        created_by = 1,
        side_a = 1,
        side_b = 2
        )
    db.add(debate)
    db.commit()
    db.refresh(debate)
    return debate