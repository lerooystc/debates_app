from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    name : str = Field(..., min_length=6)
    password : str = Field(..., min_length=8)
    email : EmailStr