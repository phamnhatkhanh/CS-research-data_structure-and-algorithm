from email.policy import default
from turtle import circle
from xmlrpc.client import DateTime
from sqlalchemy import Column, BigInteger, ForeignKey, DateTime, Integer, Boolean, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.database import Base


class Keyphrase(Base):
    __tablename__ = "keyphrase"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(200))
    create_at = Column(DateTime, server_default=func.now())
    update_at = Column(DateTime, onupdate=func.now())

    keyphrase_noidung = relationship(
        "KeyphraseNoiDung",
        back_populates="keyphrase",
        cascade="all, delete")
