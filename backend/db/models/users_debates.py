from db import Base
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer


class UserDebates(Base):
    __tablename__ = "users_to_debates"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    debate_id = Column(Integer, ForeignKey("debate.id"))
