from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from db import Base
from sqlalchemy.orm import relationship

class Debates(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    is_private = Column(Boolean, default=True)
    created_by = Column(Integer, ForeignKey("users.id"))
    side_a = Column(Integer, ForeignKey("users.id"))
    side_b = Column(Integer, ForeignKey("users.id"))
    members = relationship("User", secondary='users_to_debates', back_populates='debates')