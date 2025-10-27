from fastapi import APIRouter, HTTPException, status, Depends
from app.DB.database import get_db
from sqlalchemy.orm import Session
import app.schema.userSchema as Schemas
import app.model as models
from app.utils import hashPassword,verifyPassword

authRouter = APIRouter(
    tags=['Authentication']
)

@authRouter.post('/login/')
async def login(user_credentials : Schemas.UserLogin ,db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()
    
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = "Invalid Credentials")
    if verifyPassword(user_credentials.password , user.password):
        return "Login Sucessful"
    else:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = "Invalid Credentials")
    
    #TODO
    #create Token

    #TODO
    #return token