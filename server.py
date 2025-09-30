from fastapi import FastAPI,HTTPException,status,Response
from routes import post_router

app = FastAPI()

app.include_router(post_router)

@app.get('/',status_code=status.HTTP_200_OK)
async def health_check():
    return Response(content="Server working!!")