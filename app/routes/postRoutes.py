from fastapi import APIRouter,status,HTTPException
from app.controller import get_all_posts,get_post_by_id,create_post,update_single_post,delete_post
from app.model import Post,UpdatePost

post_router  = APIRouter()

@post_router.get('/posts/')
async def get_post():
    return await get_all_posts()

@post_router.get('/posts/{id}',status_code=status.HTTP_200_OK)
async def get_post_id(id : int):
    post =  await get_post_by_id(id)
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No post Found")
    return post


@post_router.post('/posts/',status_code = status.HTTP_201_CREATED)
async def create_new_post(new_post : Post):
    created_post : dict = await create_post(new_post)
    if create_post:
        return created_post
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@post_router.put('/posts/{id}' , status_code = status.HTTP_200_OK)
async def update_post(id : int , updated_post : UpdatePost):
    updated_post_resp = await update_single_post(id,updated_post)
    if updated_post_resp is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} not found")
    return updated_post_resp

@post_router.delete('/posts/{id}',status_code=status.HTTP_200_OK)
async def delete_a_post(id : int):
    deleted =  await delete_post(id)
    if deleted is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} not found")
    return {"detail" : f"Post with id {id} deleted"}