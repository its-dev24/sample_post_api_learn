from fastapi import FastAPI,HTTPException,status,Response
from app.routes import post_router
# from app.DB import connect_db
from app.model import tableModel
from .DB.database import engine

tableModel.Base.metadata.createall(bind = engine)



app = FastAPI()

app.include_router(post_router)

@app.get('/',status_code=status.HTTP_200_OK)
async def health_check():
    return Response(content="Server working!!") 