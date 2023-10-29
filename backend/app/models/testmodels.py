from email.policy import default
from time import time
from xmlrpc.client import DateTime
from sqlalchemy import Column, BigInteger, Integer, SmallInteger, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.database import Base


class Test(Base):
    __tablename__ = "test"

    id = Column(BigInteger, primary_key=True, index=True)
    score = Column(SmallInteger, default=0)
    id_user = Column(BigInteger, ForeignKey("user.id"))
    user = relationship("User", back_populates="test", cascade="all, delete")

    create_at = Column(DateTime, server_default=func.now())
    update_at = Column(DateTime, onupdate=func.now())

    time = Column(Integer, default=45)

    question = relationship(
        "Question",
        back_populates="test",
        cascade="all, delete")
