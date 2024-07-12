from datetime import datetime
from sqlalchemy import Column, Integer, String, TIMESTAMP
from db import Base
from sqlalchemy.orm import relationship

class Users(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    debates = relationship("Debate", secondary="users_to_debates", back_populates="members")