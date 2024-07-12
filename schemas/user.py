from pydantic import BaseModel, Field, EmailStr, ConfigDict
from datetime import datetime

class UserCreate(BaseModel):
    name : str = Field(..., min_length=6)
    password : str = Field(..., min_length=8)
    email : EmailStr
    

class ShowUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email : EmailStr
    registered_at : datetime
