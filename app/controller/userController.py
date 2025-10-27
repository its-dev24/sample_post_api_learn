from sqlalchemy.orm import Session
import app.schema.userSchema as Schema
import app.model as model
from fastapi import HTTPException,status

async def create_users(user : Schema.CreateUser , db : Session):
        existing = db.query(model.User).filter(model.User.email == user.email).first()
        if existing is not None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User Already exists")
        user_data = model.User(**user.model_dump())
        db.add(user_data)
        db.commit()
        db.refresh(user_data)
        return user_data