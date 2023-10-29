from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

SQLALCHAMY_DATABASE_URL = "mysql://root:@localhost:3306/sl-final"

# config = Configurator()
# config.scan('myapp.models')  # the "important" line
engine = create_engine(SQLALCHAMY_DATABASE_URL)
# engine = create_engine(SQLALCHAMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
