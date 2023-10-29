from email.policy import default
from turtle import circle
from xmlrpc.client import DateTime
from sqlalchemy import Column, BigInteger, ForeignKey, DateTime, Integer, Boolean, PrimaryKeyConstraint, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.database import Base


class NoiDung(Base):
    __tablename__ = "noidung"

    id = Column(BigInteger, primary_key=True, index=True)

    id_section = Column(BigInteger, ForeignKey("section.id"))
    section = relationship(
        "Section",
        back_populates="noidung",
        cascade="all, delete")

    yeu_to_tri_thuc = Column(String(200))

    content = Column(String(2000))
    order = Column(Integer, default=0)

    id_root_noidung_keyphrase = Column(
        BigInteger, ForeignKey("keyphrasenoidung.id"))
    root_noidung_keyphrase = relationship(
        "KeyphraseNoiDung",
        foreign_keys=[id_root_noidung_keyphrase],
        back_populates="noidung1",
        cascade="all, delete")

    id_relation_noidung_keyphrase = Column(
        BigInteger, ForeignKey("keyphrasenoidung.id"))
    relation_noidung_keyphrase = relationship(
        "KeyphraseNoiDung",
        foreign_keys=[id_relation_noidung_keyphrase],
        back_populates="noidung2",
        cascade="all, delete")

    type = Column(String(200))
    create_at = Column(DateTime, server_default=func.now())
    update_at = Column(DateTime, onupdate=func.now())
