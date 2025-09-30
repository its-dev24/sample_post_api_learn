from fastapi import APIRouter,status,HTTPException
from controller import get_all_posts,get_post_by_id

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