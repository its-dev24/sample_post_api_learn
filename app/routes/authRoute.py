from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from app.DB.database import get_db
from sqlalchemy.orm import Session
import app.schema.userSchema as Schemas
import app.model as models
from app.utils import verifyPassword,oauth2

authRouter = APIRouter(
    tags=['Authentication']
)

@authRouter.post('/login/')
async def login(user_credentials : OAuth2PasswordRequestForm = Depends() ,db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    
    if not user:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN,detail = "Invalid Credentials")
    if not verifyPassword(user_credentials.password , user.password):
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN,detail = "Invalid Credentials")
    else:
        access_token = oauth2.create_access_token(data = {"user_id" : user.id})
        return {"access token" : access_token , "token_type" : "bearer"}
    
    #TODO
    #return token