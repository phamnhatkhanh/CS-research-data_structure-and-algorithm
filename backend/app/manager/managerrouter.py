from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from models.questioncontentmodels import QuestionContent
from models.sectionmodels import Section
from models.chaptermodels import Chapter
from dto.userschema import RegisterUser
from .managerservice import ManagerService
from config.token import get_currentUser

from config.hashing import Hashing
from models.usermodels import User
import json
import io
router = APIRouter(prefix="/manager", tags=["Manager"])


@router.get("/seed")
def seed(db: Session = Depends(get_db)):
    return ManagerService.seed(db=db)


@router.get("/seed1")
def seed1(db: Session = Depends(get_db)):
    db.add(User(
        name="Nguyen Van Phong",
        email="phong940253@gmail.com",
        password_hash=Hashing.bcrypt("01676940253"),
        verify=True))

    f = open('data2.json', encoding='utf-8')
    data = json.load(f)
    list_chapter = [
        "dynamic programming",
        "graph traversals",
        "insertionsort",
        "analysis of algorithms (recurrences)",
        "sorting",
        "bubblesort",
        "mergesort",
        "heap",
        "recursion",
        "array",
        "graph shortest paths",
        "binary trees",
        "greedy algorithms",
        "bit algorithms",
        "tree traversals",
        "graph theory",
        "queue",
        "b and b+ trees",
        "algorithms",
        "graph minimum spanning tree",
        "searching",
        "balanced binary search trees",
        "divide and conquer",
        "linked list",
        "binary search trees",
        "analysis of algorithms",
        "radixsort",
        "stack",
        "graph"
    ]
    # list_chapter = set()
    # for i in data:
    #     if len(i['keyword']) > 0:
    #         list_chapter.add(i["keyword"][0])
    db.add_all([Chapter(name=chapter) for chapter in list_chapter])
    db.commit()

    list_section = [
        ['common dynamic programming'],
        [
            'prim',
            'dfs',
            'bfs',
            'common graph traversals',
            'shortest path',
            'dijkstra’s',
            'kruskal',
        ], [
            'insertion sort',
            'common insertionsort'],
        ['common analysis of algorithms (recurrences)'],
        ['common sorting'],
        [
            'common bubblesort'
            'bubble sort'],
        ['merge sort', 'common mergesort'],
        ['heap sort', 'common heap', 'binary heap', 'max-heap', 'min-heap'],
        [],  # recursion,
        [],  # array,
        [],  # "graph shortest paths",
        [],  # "binary trees",
        [],  # "greedy algorithms",
        [],  # "bit algorithms",
        [],  # "tree traversals",
        ['common graph'],  # "graph theory",
        [],  # "queue",
        [],  # "b and b+ trees",
        [],  # "algorithms",
        [],  # "graph minimum spanning tree",
        [],  # "searching",
        [],  # "balanced binary search trees",
        [],  # "divide and conquer",
        ['common linked list'],  # "linked list",
        [],  # "binary search trees",
        [],  # "analysis of algorithms",
        [],  # "radixsort",
        ['common stack'],  # "stack",
        ['common graph', 'common graph theory']  # "graph"


        # [,
        #  'common b and b+ trees',
        #
        ,  # 'backtracking',
        #  ,
        #  'common selectionsort',
        #  ,
        #  'common quicksort',
        #  'jump search',
        #  'common bit algorithms',
        #
        #  'exponential search',
        #  'common heap',
        #  'common binary search trees',
        #  'common balanced binary search trees',

        #  'recursion',
        #  'directed',
        #  'arrangement',
        #  'radix sort',
        #  ,
        #  'common radixsort',
        #  'selection sort',
        #  ,
        #  'common recursion',
        #  'common binary trees',
        #  'common heapsort',
        #  'singly',
        #  'dynamic programming',
        #  'interpolation search',
        #  'binary search tree',
        #  'array rotations',
        #  'huffman coding',
        #  'common tree traversals',
        #  'balanced binary search tree',
        #  'common divide and conquer',
        #  'common searching',
        #  'common countingsort',
        #  'common binarysearch',
        #  ,
        #  'minimum spanning tree',
        # ,
        #  'common linked list',
        #  'common greedy algorithms',
        #  ,
        #  'quicksort',
        #  'undirected',
        #  'common queue',
        #  'circular',
        #  'doubly',
        #  'linear search',
        #  'common array',
        #  'common analysis of algorithms',
        #  'common algorithms',
        #  'min-heap',
        #  'binary search',
        #  'common graph shortest paths',
        #  'common c arrays']
    ]
    list_data_section = []
    for index, section in enumerate(list_section):
        for data in section:
            list_data_section.append(
                Section(name=data, id_chapter=index + 1))
    db.add_all(list_data_section)
    db.commit()

    f = open('data2.json', encoding='utf-8')
    data = json.load(f)
    list_question_content = []
    for question_content in data:
        if len(question_content['sections']) > 0:
            db_section = db.query(Section).filter(
                Section.name == question_content["sections"][0]).first()
            if db_section is not None and len(question_content['answer']) == 4:
                db_section_id = db_section.id
                list_question_content.append(
                    QuestionContent(
                        content=question_content["question"],
                        correct_answer=question_content["correct"],
                        answer_a=question_content["answer"][0],
                        answer_b=question_content["answer"][1],
                        answer_c=question_content["answer"][2],
                        answer_d=question_content["answer"][3],
                        explain=question_content["explain"],
                        id_section=db_section_id,
                    ))
    db.add_all(list_question_content)
    db.commit()

    return list_chapter

# @router.get("/")
# def getAllUser(db: Session = Depends(get_db)):
#     return UserService.get_allUser(db=db)


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
