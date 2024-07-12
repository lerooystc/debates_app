from pydantic import BaseModel, Field, EmailStr, ConfigDict, root_validator
from datetime import datetime
import random
import string

class DebateCreate(BaseModel):
    name : str = Field(..., min_length=6)
    access_code : str
    is_private: bool
    
    @root_validator(pre=True)
    def generate_access_code(cls, values):
        values['access_code'] = ''.join(random.choices(string.ascii_uppercase, k=16))
        print(values)
        return values
    

class ShowDebate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name : str = Field(..., min_length=6)
    is_private: bool
    created_at : datetime
    access_code : str