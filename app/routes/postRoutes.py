from fastapi import APIRouter,status,HTTPException,Depends
from app.controller import get_all_posts,get_post_by_id,create_post,delete_post,update_single_post,get_current_user_post
from app.schema import Post,UpdatePost,createPost,PostResp
from app.DB.database import get_db
from sqlalchemy.orm import Session
from typing import List
from app.utils import oauth2

post_router  = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@post_router.get('/',response_model=List[PostResp])
async def get_post( db : Session = Depends(get_db)):
    return await get_all_posts(db)

@post_router.get('/current_user', response_model = List[PostResp])
async def get_user_post(db : Session = Depends(get_db) , current_user = Depends(oauth2.get_current_user)):
    posts = await get_current_user_post(current_user=current_user , db = db)
    if posts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No post Found")
    return posts

@post_router.get('/{id}',status_code=status.HTTP_200_OK , response_model= PostResp)
async def get_post_id(id : int ,  db : Session = Depends(get_db),current_user = Depends(oauth2.get_current_user)):
    post =  await get_post_by_id(id,db)
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No post Found")
    return post


@post_router.post('/',status_code = status.HTTP_201_CREATED,response_model=PostResp)
async def create_new_post(new_post : createPost, db : Session = Depends(get_db),current_user = Depends(oauth2.get_current_user)):
    created_post = await create_post(new_post,current_user,db)
    if created_post:
        return created_post
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@post_router.put('/{id}' , status_code = status.HTTP_200_OK,response_model = PostResp)
async def update_post(id : int , updated_post : UpdatePost , db : Session = Depends(get_db),current_user = Depends(oauth2.get_current_user)):
    updated_post_resp = await update_single_post(id,current_user,updated_post,db)
    if updated_post_resp is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} not found")
    return updated_post_resp

@post_router.delete('/{id}',status_code=status.HTTP_200_OK)
async def delete_a_post(id : int , db : Session = Depends(get_db),current_user = Depends(oauth2.get_current_user)):
    deleted =  await delete_post(id,current_user,db)
    if deleted is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} not found")
    return {"detail" : f"Post with id {id} deleted"}