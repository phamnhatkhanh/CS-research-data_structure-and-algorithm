from email.policy import default
from enum import unique
from xmlrpc.client import DateTime
from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(50), unique=True)
    date_of_birth = Column(DateTime)
    password_hash = Column(String(200))
    verify_at = Column(DateTime)
    verify = Column(Boolean, default=False)
    create_at = Column(DateTime, server_default=func.now())
    update_at = Column(DateTime, onupdate=func.now())

    test = relationship("Test", back_populates="user", cascade="all, delete")
