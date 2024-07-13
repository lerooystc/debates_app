from sqlalchemy.orm import Session
from schemas.debate import CreateDebate, UpdateDebate
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

def create_new_debate(debate: CreateDebate, db: Session):
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

def list_public_debates(db: Session):
    debates = db.query(Debate).filter(Debate.is_private == False).all()
    return debates

def update_debate(code: str, debate: UpdateDebate, db: Session):
    old_debate = db.query(Debate).filter(Debate.access_code == code).first()
    if not old_debate:
        return
    old_debate.finished = debate.finished
    db.add(old_debate)
    db.commit()
    return old_debate

def delete_debate(code: str, db: Session):
    debate = db.query(Debate).filter(Debate.access_code == code)
    if not debate.first():
        return {"error": "Couldn't find the debate."}
    debate.delete()
    db.commit()
    return {"msg": "Successfully deleted the debate."}
