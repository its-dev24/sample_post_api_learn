from fastapi import APIRouter,status,HTTPException
from controller import get_all_posts,get_post_by_id,create_post
from model import Post

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