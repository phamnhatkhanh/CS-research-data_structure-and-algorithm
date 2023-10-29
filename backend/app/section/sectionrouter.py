from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from models.usermodels import User
from dto.userschema import RegisterUser
from .sectionservice import SectionService
from config.token import get_currentUser

router = APIRouter(prefix="/section", tags=["Section"])


@router.get("/")
def getAllSection(db: Session = Depends(get_db)):
    return SectionService.get_allSection(db=db)


# @router.post("/")
# def createUser(user: RegisterUser, db: Session = Depends(get_db)):
#     return UserService.create_user(user, db)


# @router.get("/me")
# def getMe(current_user: User = Depends(get_currentUser)):
#     return current_user


# @router.put("/{userid}")
# def updateUser(userid: int, user: RegisterUser, db: Session = Depends(get_db)):
#     return UserService.update_user(userid=userid, user=user, db=db)


# @router.delete("/{userid}")
# def deleteUser(userid: int, db: Session = Depends(get_db)):
#     return UserService.deleteUser(userid=userid, db=db)
