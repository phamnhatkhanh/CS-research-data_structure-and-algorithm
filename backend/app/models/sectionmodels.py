from email.policy import default
from turtle import circle
from xmlrpc.client import DateTime
from sqlalchemy import Column, BigInteger, ForeignKey, DateTime, Integer, Boolean, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.database import Base


class Section(Base):
    __tablename__ = "section"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(200))
    order = Column(Integer, default=0)
    id_chapter = Column(BigInteger, ForeignKey("chapter.id"))
    chapter = relationship(
        "Chapter",
        back_populates="section",
        cascade="all, delete")
    create_at = Column(DateTime, server_default=func.now())
    update_at = Column(DateTime, onupdate=func.now())

    noidung = relationship("NoiDung", back_populates="section")
    questioncontent = relationship("QuestionContent", back_populates="section")
