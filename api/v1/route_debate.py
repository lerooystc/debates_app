from fastapi import APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from schemas.debate import CreateDebate, ShowDebate, UpdateDebate
from db.session import get_db
from db.repository.debate import create_new_debate, retrieve_debate, list_public_debates, update_debate, delete_debate
from typing import List

router = APIRouter()

@router.post("/debates", response_model=ShowDebate, status_code=status.HTTP_201_CREATED)
async def create_debate(debate: CreateDebate, db: Session = Depends(get_db)):
    debate = create_new_debate(debate=debate,db=db, created_by=1)
    return debate

@router.get("/debates/{code}", response_model=ShowDebate, status_code=status.HTTP_200_OK)
async def get_debate(code: str, db: Session = Depends(get_db)):
    debate = retrieve_debate(code=code, db=db)
    if not debate:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Debate not found.")
    return debate

@router.get("/debates", response_model=List[ShowDebate], status_code=status.HTTP_200_OK)
async def get_public_debates(db: Session = Depends(get_db)):
    debates = list_public_debates(db=db)
    return debates

@router.put("/debates/{code}", response_model=ShowDebate, status_code=status.HTTP_200_OK)
async def update_a_debate(code: str, debate: UpdateDebate, db: Session = Depends(get_db)):
    debate = update_debate(code=code, debate=debate, db=db)
    if not debate:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Debate not found.")
    return debate

@router.delete("/debates/{code}")
async def delete_a_debate(code: str, db: Session = Depends(get_db)):
    message = delete_debate(code=code, db=db)
    if message.get("error"):
        raise HTTPException(detail=message.get("error"), status_code= status.HTTP_400_BAD_REQUEST)
    return message.get("msg")
