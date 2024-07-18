from typing import List

from api.v1.route_login import get_current_user
from db import User
from db.repository.debate import create_new_debate
from db.repository.debate import delete_debate
from db.repository.debate import list_public_debates
from db.repository.debate import retrieve_debate
from db.repository.debate import update_debate
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from schemas.debate import CreateDebate
from schemas.debate import ShowDebate
from schemas.debate import UpdateDebate
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/debates", response_model=ShowDebate, status_code=status.HTTP_201_CREATED)
async def create_debate(
    debate: CreateDebate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    debate = create_new_debate(debate=debate, db=db, created_by=current_user.id)
    return debate


@router.get(
    "/debates/{code}", response_model=ShowDebate, status_code=status.HTTP_200_OK
)
async def get_debate(code: str, db: Session = Depends(get_db)):
    debate = retrieve_debate(code=code, db=db)
    if not debate:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Debate not found."
        )
    return debate


@router.get("/debates", response_model=List[ShowDebate], status_code=status.HTTP_200_OK)
async def get_public_debates(db: Session = Depends(get_db)):
    debates = list_public_debates(db=db)
    return debates


@router.put(
    "/debates/{code}", response_model=ShowDebate, status_code=status.HTTP_200_OK
)
async def update_a_debate(
    code: str,
    debate: UpdateDebate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    debate = update_debate(code=code, debate=debate, created_by=current_user.id, db=db)
    if isinstance(debate, dict):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Debate not found."
        )
    return debate


@router.delete("/debates/{code}")
async def delete_a_debate(
    code: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    message = delete_debate(code=code, created_by=current_user.id, db=db)
    if message.get("error"):
        raise HTTPException(
            detail=message.get("error"), status_code=status.HTTP_400_BAD_REQUEST
        )
    return message.get("msg")
