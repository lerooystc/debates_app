from pydantic import BaseModel, Field, EmailStr, ConfigDict, root_validator
from datetime import datetime


class CreateDebate(BaseModel):
    name : str = Field(..., min_length=6)
    is_private: bool
    

class ShowDebate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name : str = Field(..., min_length=6)
    is_private: bool
    created_at : datetime
    access_code : str
    finished: bool
    
class UpdateDebate(CreateDebate):
    finished : bool