if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    
import time
from urllib.request import Request
from fastapi import FastAPI
from config.database import engine
from auth import authrouter
from users import usersrouter
from chapter import chapterrouter
from tests import testrouter
from section import sectionrouter
from questioncontent import questioncontentrouter
from noidung import noidungrouter
from keyphrase import keyphraserouter
from manager import managerrouter
from keyphrasenoidung import keyphrasenoidungrouter
from question import questionrouter
from models import initialize_sql
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

initialize_sql(engine)


@app.get("/")
async def hello():
    return "Hello"

app.include_router(authrouter.router)
app.include_router(usersrouter.router)
app.include_router(testrouter.router)
app.include_router(questionrouter.router)
app.include_router(questioncontentrouter.router)
app.include_router(noidungrouter.router)
app.include_router(chapterrouter.router)
app.include_router(sectionrouter.router)
app.include_router(keyphraserouter.router)
app.include_router(keyphrasenoidungrouter.router)
app.include_router(managerrouter.router)

