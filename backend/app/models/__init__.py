from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.sql import func
from sqlalchemy import Column, BigInteger, ForeignKey, DateTime
from config.database import Base

from .noidungmodels import NoiDung
from .keyphrasenoidungmodels import KeyphraseNoiDung

DBSession = scoped_session(sessionmaker())


def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(bind=engine)
