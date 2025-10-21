from fastapi import FastAPI,HTTPException,status,Response,Depends
from app.routes import post_router
# from app.DB import connect_db
from app.model import tableModel
from .DB.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.utils import lifespan


app = FastAPI(lifespan=lifespan)


app.include_router(post_router)

@app.get('/',status_code=status.HTTP_200_OK)
async def health_check(db:Session  = Depends(get_db)):
    try : 
        db.execute(text("SELECT 1"))
        return Response(content="Server working!!") 
    except Exception as e: 
        raise HTTPException(status_code=500 ,detail=str(e))