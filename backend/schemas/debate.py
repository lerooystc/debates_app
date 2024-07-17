from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class CreateDebate(BaseModel):
    name: str = Field(..., min_length=6)
    is_private: bool


class ShowDebate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str = Field(..., min_length=6)
    is_private: bool
    created_at: datetime
    access_code: str
    finished: bool


class UpdateDebate(CreateDebate):
    finished: bool
