from datetime import datetime
from datetime import UTC

from db import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import relationship


class User(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.now(UTC))
    debates = relationship(
        "Debate", secondary="users_to_debates", back_populates="members"
    )
