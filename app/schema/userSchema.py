from pydantic import BaseModel,EmailStr
from datetime import datetime
class UserBase(BaseModel):
    email : EmailStr
    

class CreateUser(UserBase):
    password : str

class UserResp(UserBase):
    id : int
    created_at : datetime
    pass

    class Config:
        orm_mode = True