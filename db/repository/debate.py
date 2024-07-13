from sqlalchemy.orm import Session
from schemas.debate import DebateCreate
from db.models.debate import Debate
import random
import string

def retrieve_debate(code: str, db: Session):
    debate = db.query(Debate).filter(Debate.access_code == code).first()
    return debate

def generate_access_code(db : Session):
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=16))
        if not retrieve_debate(code, db):
            break
    return code

def create_new_debate(debate: DebateCreate, db: Session):
    debate = Debate(
        **debate.model_dump(),
        access_code = generate_access_code(db),
        created_by = 1,
        side_a = 1,
        side_b = 2
        )
    db.add(debate)
    db.commit()
    db.refresh(debate)
    return debate

