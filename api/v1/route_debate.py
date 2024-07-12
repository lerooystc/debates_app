from fastapi import APIRouter, status
from sqlalchemy.orm import Session
from fastapi import Depends
from schemas.debate import DebateCreate, ShowDebate
from db.session import get_db
from db.repository.debate import create_new_debate 

router = APIRouter()

@router.post("/", response_model=ShowDebate, status_code=status.HTTP_201_CREATED)
async def create_debate(debate: DebateCreate, db: Session = Depends(get_db)):
    debate = create_new_debate(debate=debate,db=db)
    return debate
