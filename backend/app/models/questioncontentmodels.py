from email.policy import default
from turtle import circle
from xmlrpc.client import DateTime
from sqlalchemy import Column, BigInteger, ForeignKey, DateTime, Integer, Boolean, PrimaryKeyConstraint, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.database import Base


class QuestionContent(Base):
    __tablename__ = "questioncontent"

    id = Column(BigInteger, primary_key=True, index=True)
    # id_chapter = Column(BigInteger, ForeignKey("chapter.id"))
    # chapter = relationship(
    #     "Chapter",
    #     back_populates="noidung",
    #     cascade="all, delete")

    id_section = Column(BigInteger, ForeignKey("section.id"))
    section = relationship(
        "Section",
        back_populates="questioncontent",
        cascade="all, delete")

    content = Column(String(2000))
    answer_a = Column(String(2000))
    answer_b = Column(String(2000))
    answer_c = Column(String(2000))
    answer_d = Column(String(2000))
    explain = Column(String(2000))

    order = Column(Integer, default=0)

    correct_answer = Column(String(200))
    create_at = Column(DateTime, server_default=func.now())
    update_at = Column(DateTime, onupdate=func.now())

    question = relationship(
        "Question",
        back_populates="questioncontent",
        cascade="all, delete")
