from sqlalchemy.orm import Session
import app.schema.userSchema as Schema
import app.model as model
from fastapi import HTTPException,status
from app.utils import hashPassword

async def create_users(user : Schema.CreateUser , db : Session):
        existing = db.query(model.User).filter(model.User.email == user.email).first()
        if existing is not None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User Already exists")
        user.password = hashPassword(user.password)
        print(f"Password before hashing {type(user.password)}")
        user_data = model.User(**user.model_dump())
        try:
            db.add(user_data)
            db.commit()
            db.refresh(user_data)
            return user_data
        except Exception as e:
              db.rollback()
              raise

async def retrive_user(id : int , db : Session):
      user = db.query(model.User).filter(model.User.id == id).first()
      return user
