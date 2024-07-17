from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, TIMESTAMP
from db import Base
from sqlalchemy.orm import relationship
from datetime import datetime, UTC

class Debate(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    is_private = Column(Boolean, default=True)
    access_code = Column(String)
    created_by = Column(Integer, ForeignKey("user.id"))
    created_at = Column(TIMESTAMP, default=datetime.now(UTC))
    side_a = Column(Integer, ForeignKey("user.id"))
    side_b = Column(Integer, ForeignKey("user.id"))
    members = relationship("User", secondary='users_to_debates', back_populates='debates')
    finished = Column(Boolean, default=False)