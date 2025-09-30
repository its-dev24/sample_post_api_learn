from DB import POSTS
from utils import queryId
from model import Post

async def get_all_posts():
    return POSTS

async def get_post_by_id(id : int):
    post = queryId(POSTS , id)
    return post

# async def create_post(new_post : Post):

