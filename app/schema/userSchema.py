from pydantic import BaseModel,EmailStr

class UserBase(BaseModel):
    email : EmailStr
    

class CreateUser(UserBase):
    password : str

class UserResp(UserBase):
    id : int
    pass

    class Config:
        orm_mode = True