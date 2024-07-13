from fastapi import APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from schemas.debate import DebateCreate, ShowDebate
from db.session import get_db
from db.repository.debate import create_new_debate, retrieve_debate

router = APIRouter()

@router.post("/debates", response_model=ShowDebate, status_code=status.HTTP_201_CREATED)
async def create_debate(debate: DebateCreate, db: Session = Depends(get_db)):
    debate = create_new_debate(debate=debate,db=db)
    return debate

@router.get("/debates/{code}", response_model=ShowDebate, status_code=status.HTTP_200_OK)
async def get_debate(code: str, db: Session = Depends(get_db)):
    debate = retrieve_debate(code=code, db=db)
    if not debate:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Debate not found.")
    return debate