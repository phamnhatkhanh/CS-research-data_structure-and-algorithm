from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.questioncontentmodels import QuestionContent
from models.questionmodels import Question
from config.database import get_db
from dto.sectionschema import SectionId
from dto.testschema import TestValid
from .testservice import TestService
from sqlalchemy import select
from sqlalchemy.sql import func
from models.sectionmodels import Section
from models.testmodels import Test

router = APIRouter(prefix="/tests", tags=["Tests"])


@router.get("/")
def get_all_test(db: Session = Depends(get_db)):
    return TestService.get_all_test(db=db)


@router.post("/")
def create_test(
        section: SectionId,
        db: Session = Depends(get_db)):
    db_test = TestService.create_test(
        db=db, id_user=section.id_user, time=section.time)

    db_question_content = db.execute(
        select(QuestionContent).join(Section).where(
            Section.id.in_(
                section.list_id)).order_by(
            func.rand()).limit(20)).all()
    list_question = [
        Question(
            id_test=db_test.id,
            id_question_content=question_content["QuestionContent"].id) for question_content in db_question_content]
    db.add_all(list_question)
    db.commit()

    return {"question": db.query(
        Question,
        QuestionContent.content,
        QuestionContent.answer_a,
        QuestionContent.answer_b,
        QuestionContent.answer_c,
        QuestionContent.answer_d).join(Section).join(Question).filter(
        Question.id_test == db_test.id).all(),
        "test": db_test}


@router.post("/{id_test}")
def update_test(
        test: TestValid,
        id_test: int,
        db: Session = Depends(get_db)):
    db_test = db.query(Question, QuestionContent.correct_answer).join(
        QuestionContent).join(Test).filter(Test.id == id_test).all()
    num_correct_answer = 0
    for question in db_test:
        answer_client = None
        for answer in test.list_answer:
            if answer["id"] == question.Question.id:
                answer_client = answer
                break
        if answer_client is not None:
            if answer_client["answer"] == question.correct_answer:
                question.Question.correct = True
                num_correct_answer += 1
            else:
                question.Question.correct = False
    db_test1 = db.query(Test).filter(Test.id == id_test).first()
    db_test1.score = num_correct_answer / len(db_test) * 10
    db.commit()
    db.refresh(db_test1)
    score = float(num_correct_answer / len(db_test)) * 10

    return {'score': score}


# @router.get("/me")
# def getMe(current_user: User = Depends(get_currentUser)):
#     return current_user


# @router.put("/{userid}")
# def updateUser(userid: int, user: RegisterUser, db: Session = Depends(get_db)):
#     return UserService.update_user(userid=userid, user=user, db=db)


# @router.delete("/{userid}")
# def deleteUser(userid: int, db: Session = Depends(get_db)):
#     return UserService.deleteUser(userid=userid, db=db)
