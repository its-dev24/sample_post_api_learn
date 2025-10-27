from sqlalchemy.orm import Session
import app.schema.userSchema as Schema
import app.model as model

async def create_users(user : Schema.CreateUser , db : Session):
    user_data = model.User(**user.model_dump())
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    return user_data