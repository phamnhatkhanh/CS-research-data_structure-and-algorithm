import email
from multiprocessing.connection import answer_challenge
from fastapi import Depends
from models.questioncontentmodels import QuestionContent
from config.database import get_db

from models.chaptermodels import Chapter
from models.sectionmodels import Section
from sqlalchemy.orm import Session
from config.hashing import Hashing
from models.usermodels import User


class ManagerService:
    def seed(db: Session):
        db.add(User(
            name="Nguyen Van Phong",
            email="phong940253@gmail.com",
            password_hash=Hashing.bcrypt("01676940253"),
            verify=True))

        list_chapter = [
            "Array",
            "Linked List",
            "Stack",
            "Queue",
            "Binary Tree",
            "Binary Search Tree",
            "Heap",
            "Hashing",
            "Graph"
        ]
        db.add_all([Chapter(name=chapter) for chapter in list_chapter])
        db.commit()

        list_section = [
            [
                "Array Rotations",
                "Arrangement Rearrangement",
                "Order Statistics",
                "Range Queries",
                "Optimization Problems",
                "Array Sorting",
                "Array Searching"
            ],
            [
                "Singly Linked List",
                "Doubly Linked List",
            ]
        ]
        list_data_section = []
        for index, section in enumerate(list_section):
            for data in section:
                list_data_section.append(
                    Section(name=data, id_chapter=index + 1))
        db.add_all(list_data_section)
        db.commit()

        list_question_content = [{
            "question": "What does the following function do for a given Linked List with first node as head?\r\n\r\n\r\nvoid fun1(struct node* head)\r\n{\r\n  if(head == NULL)\r\n    return;\r\n  \r\n  fun1(head->next);\r\n  printf(\"%d  \", head->data);\r\n}\r\n",
            "answer": [
                "Prints all nodes of linked lists",
                "Prints all nodes of linked list in reverse order",
                "Prints alternate nodes of Linked List",
                "Prints alternate nodes in reverse order"
            ],
            "correct": "B",
            "explain": "<div class=\"mtq_explanation-text\"> fun1() prints the given Linked List in reverse manner. For Linked List 1-&gt;2-&gt;3-&gt;4-&gt;5, fun1() prints 5-&gt;4-&gt;3-&gt;2-&gt;1.   See <a href=\"http://www.geeksforgeeks.org/practice-questions-for-linked-list-and-recursion/\" target=\"_blank\">http://www.geeksforgeeks.org/practice-questions-for-linked-list-and-recursion/</a></div>",
            "keyword": "Linked List",
            "section": "Singly Linked List"
        },
            {
            "question": "Consider the following function that takes reference to head of a Doubly Linked List as parameter.   Assume that a node of doubly linked list has previous pointer as prev and next pointer as next.  \r\n\r\n\r\nvoid fun(struct node **head_ref)\r\n{\r\n    struct node *temp = NULL;\r\n    struct node *current = *head_ref;\r\n\r\n    while (current !=  NULL)\r\n    {\r\n        temp = current->prev;\r\n        current->prev = current->next;\r\n        current->next = temp;\r\n        current = current->prev;\r\n    }\r\n\r\n    if(temp != NULL )\r\n        *head_ref = temp->prev;\r\n}\r\n\r\n\r\nAssume that reference of head of following doubly linked list is passed to above function\r\n\r\n1 <--> 2 <--> 3 <--> 4 <--> 5 <-->6.\r\n\r\nWhat should be the modified linked list after the function call?",
            "answer": [
                "2 <--> 1 <--> 4 <--> 3 <--> 6 <-->5",
                "5 <--> 4 <--> 3 <--> 2 <--> 1 <-->6.",
                "6 <--> 5 <--> 4 <--> 3 <--> 2 <--> 1.",
                "6 <--> 5 <--> 4 <--> 3 <--> 1 <--> 2"
            ],
            "correct": "C",
            "explain": "<div class=\"mtq_explanation-text\"> The given function reverses the given doubly linked list.   See <a href=\"http://www.geeksforgeeks.org/reverse-a-doubly-linked-list/\" target=\"_blank\">Reverse a Doubly Linked List</a> for details.</div>",
            "section": "Doubly Linked List"
        },
            {
            "question": "Which of the following sorting algorithms can be used to sort a random linked list with minimum time complexity?",
            "answer": [
                "Insertion Sort",
                "Quick Sort",
                "Heap Sort",
                "Merge Sort"
            ],
            "correct": "D",
            "explain": "<div class=\"mtq_explanation-text\"> Both Merge sort and Insertion sort can be used for linked lists. \r\n\r\nThe slow random-access performance of a linked list makes other algorithms (such as quicksort) perform poorly, and others (such as heapsort) completely impossible.\r\n\r\nSince worst case time complexity of Merge Sort is O(nLogn) and Insertion sort is O(n^2), merge sort is preferred.\r\n\r\nSee following for implementation of merge sort using Linked List. \r\n\r\n<a href=\"http://www.geeksforgeeks.org/merge-sort-for-linked-list/\">http://www.geeksforgeeks.org/merge-sort-for-linked-list/</a></div>",
            "section": "Array Sorting"
        }, ]

        db.add_all([QuestionContent(
            content=question_content["question"],
            correct_answer=question_content["correct"],
            answer_a=question_content["answer"][0],
            answer_b=question_content["answer"][1],
            answer_c=question_content["answer"][2],
            answer_d=question_content["answer"][3],
            explain=question_content["explain"],
            id_section=db.query(Section).filter(Section.name == question_content["section"]).first().id,
        )
            for question_content in list_question_content])
        db.commit()
        return []
    # def get_allUser(db: Session):
    #     return db.query(Chapter).all()

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
