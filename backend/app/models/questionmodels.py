from email.policy import default
from turtle import back
from xmlrpc.client import DateTime
from sqlalchemy import Column, BigInteger, ForeignKey, DateTime, Integer, Boolean, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.database import Base


class Question(Base):
    __tablename__ = "question"

    id = Column(BigInteger, primary_key=True, index=True)
    id_test = Column(BigInteger, ForeignKey("test.id"))
    test = relationship(
        "Test",
        back_populates="question",
        cascade="all, delete")
    id_question_content = Column(BigInteger, ForeignKey("questioncontent.id"))
    order = Column(Integer, default=0)
    create_at = Column(DateTime, server_default=func.now())
    update_at = Column(DateTime, onupdate=func.now())
    correct = Column(Boolean, default=False)

    questioncontent = relationship(
        "QuestionContent",
        back_populates="question",
        cascade="all, delete")
