from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from models.usermodels import User
from dto.userschema import RegisterUser
from .chapterservice import ChapterService
from section.sectionservice import SectionService
from config.token import get_currentUser

router = APIRouter(prefix="/chapter", tags=["Chapter"])


@router.get("/")
def getAllChapter(db: Session = Depends(get_db)):
    return ChapterService.get_allChapter(db=db)


@router.get("/section")
def getAllChapterSection(db: Session = Depends(get_db)):
    return {"chapter": ChapterService.get_allChapter(db=db),
            "section": SectionService.get_allSection(db=db)}

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
