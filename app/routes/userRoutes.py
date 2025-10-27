from fastapi import APIRouter,HTTPException,Depends,status
import app.schema.userSchema as Schema
from app.DB.database import get_db
from sqlalchemy.orm import Session
from app.controller import create_users

user_router = APIRouter()


@user_router.post('/users',status_code=status.HTTP_201_CREATED,response_model = Schema.UserResp)
async def create_user(user :Schema.CreateUser,db : Session = Depends(get_db)):
    user = await create_users(user , db)
    if user == None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Unable to create User')
    return user