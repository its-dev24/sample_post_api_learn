from fastapi import APIRouter,status,HTTPException,Depends
from app.controller import get_all_posts,get_post_by_id,create_post,delete_post,update_single_post
from app.schema import Post,UpdatePost
from app.DB.database import get_db
from sqlalchemy.orm import Session


post_router  = APIRouter()

@post_router.get('/posts/')
async def get_post( db : Session = Depends(get_db)):
    return await get_all_posts(db)

@post_router.get('/posts/{id}',status_code=status.HTTP_200_OK)
async def get_post_id(id : int ,  db : Session = Depends(get_db)):
    post =  await get_post_by_id(id,db)
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No post Found")
    return post


@post_router.post('/posts/',status_code = status.HTTP_201_CREATED)
async def create_new_post(new_post : Post, db : Session = Depends(get_db)):
    created_post = await create_post(new_post,db)
    if create_post:
        return created_post
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@post_router.put('/posts/{id}' , status_code = status.HTTP_200_OK)
async def update_post(id : int , updated_post : UpdatePost , db : Session = Depends(get_db)):
    updated_post_resp = await update_single_post(id,updated_post,db)
    if updated_post_resp is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} not found")
    return updated_post_resp

@post_router.delete('/posts/{id}',status_code=status.HTTP_200_OK)
async def delete_a_post(id : int , db : Session = Depends(get_db)):
    deleted =  await delete_post(id,db)
    if deleted is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} not found")
    return {"detail" : f"Post with id {id} deleted"}