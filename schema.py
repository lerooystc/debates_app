from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    password: str
    email: str
    is_programmer: bool


class Idea(BaseModel):
    id: int
    created_by: User
    title: str
    description: str
