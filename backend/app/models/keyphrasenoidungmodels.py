from email.policy import default
from turtle import circle
from xmlrpc.client import DateTime
from sqlalchemy import Column, BigInteger, ForeignKey, DateTime, Integer, Boolean, PrimaryKeyConstraint, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.database import Base
from .noidungmodels import NoiDung


class KeyphraseNoiDung(Base):
    __tablename__ = "keyphrasenoidung"
    id = Column(BigInteger, primary_key=True, index=True)

    id_keyphrase = Column(
        BigInteger,
        ForeignKey("keyphrase.id"))
    id_noidung = Column(BigInteger, ForeignKey("noidung.id"))

    create_at = Column(DateTime, server_default=func.now())
    update_at = Column(DateTime, onupdate=func.now())

    keyphrase = relationship(
        "Keyphrase",
        back_populates="keyphrase_noidung",
        cascade="all, delete")

    noidung1 = relationship(
        "NoiDung",
        foreign_keys=[NoiDung.id_root_noidung_keyphrase],
        back_populates="root_noidung_keyphrase",
        cascade="all, delete")

    noidung2 = relationship(
        "NoiDung",
        foreign_keys=[NoiDung.id_relation_noidung_keyphrase],
        back_populates="relation_noidung_keyphrase",
        cascade="all, delete")
