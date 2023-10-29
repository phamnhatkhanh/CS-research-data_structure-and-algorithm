from fastapi import Depends
from config.database import get_db

from models.testmodels import Test
from sqlalchemy.orm import Session
from config.hashing import Hashing
from config.token import get_currentUser
from models.usermodels import User


class TestService:

    def get_all_test(db: Session):
        return db.query(Test).all()

    def create_test(
            db: Session,
            id_user,
            time: int = 45):
        db_test = Test(time=time, id_user=id_user)
        db.add(db_test)
        db.commit()

        db.refresh(db_test)
        return db_test

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
