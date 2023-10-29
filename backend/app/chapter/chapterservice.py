from fastapi import Depends
from config.database import get_db

from models.chaptermodels import Chapter
from sqlalchemy.orm import Session
from models.sectionmodels import Section


class ChapterService:

    def get_allChapter(db: Session):
        return db.query(Chapter.id, Chapter.name).all()

    # def get_user(email: str, db: Session = Depends(get_db)):
    #     return db.query(Chapter).filter(Chapter.email == email).first()

    # def create_user(user: RegisterUser, db: Session = Depends(get_db)):
    #     db_user = Chapter(
    #         name=Chapter.name,
    #         email=Chapter.email,
    #         password=Hashing.bcrypt(Chapter.password),
    #         is_staff=Chapter.is_staff,
    #         is_active=Chapter.is_active,
    #     )

    #     db.add(db_user)
    #     db.commit()

    #     db.refresh(db_user)
    #     db_user.password = None

    #     return db_user

    # def update_user(userid: int, user: RegisterUser, db: Session):
    #     db_userid = db.query(User).filter(User.id == userid).first()

    #     db_userid.name = user.name
    #     db_userid.email = user.email
    #     db_userid.password = Hashing.bcrypt(user.password)
    #     db_userid.is_staff = user.is_staff
    #     db_userid.is_active = user.is_active

    #     db.commit()

    #     return db_userid

    # def deleteUser(userid: int, db: Session):
    #     db_userid = db.query(User).filter(User.id == userid).first()

    #     db.delete(db_userid)

    #     db.commit()

    #     return db_userid