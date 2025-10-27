from fastapi import APIRouter,HTTPException,Depends,status
import app.schema.userSchema as Schema
from app.DB.database import get_db
from sqlalchemy.orm import Session
from app.controller import create_users,retrive_user

user_router = APIRouter(
    prefix="/users",
    tags=['User']
)


@user_router.post('/',status_code=status.HTTP_201_CREATED,response_model = Schema.UserResp)
async def create_user(user :Schema.CreateUser,db : Session = Depends(get_db)):
    user = await create_users(user , db)
    if user == None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Unable to create User')
    return user

@user_router.get('/{id}', status_code = status.HTTP_200_OK,response_model=Schema.UserResp)
async def get_user(id : int , db : Session = Depends(get_db)):
    user = await retrive_user(id,db)
    if user is None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return user