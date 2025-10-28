from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.model import tableModel
from app.DB.database import engine
from pwdlib import PasswordHash

pass_context = PasswordHash.recommended()

def queryId(dataList : list , id : int):
    for idx , item in enumerate(dataList):
        if item.get('id') == id:
            return idx , item
    return 0 ,None

@asynccontextmanager
async def lifespan(app : FastAPI):
    print('Starting server up!')
    try:

        tableModel.Base.metadata.create_all(bind = engine)
        print("Table created!1")
    except Exception as e:
        print(f"Error creating table , {e}")
    yield

    print("Shutting down")

def hashPassword(password : str ) -> str:
    return pass_context.hash(password)

def verifyPassword(user_password :str , hashed_password) -> bool:
    return pass_context.verify(user_password,hashed_password)