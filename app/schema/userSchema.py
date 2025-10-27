from pydantic import BaseModel,EmailStr

class UserBase(BaseModel):
    email : EmailStr
    password : str

class CreateUser(UserBase):
    pass

