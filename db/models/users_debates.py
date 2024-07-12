from sqlalchemy import Column, Integer, ForeignKey
from db import Base

class UserDebates(Base):
  __tablename__ = "users_to_debates"
  
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey("users.id"))
  debate_id = Column(Integer, ForeignKey("debates.id"))