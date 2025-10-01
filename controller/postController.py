from DB import POSTS
from utils import queryId
from model import Post

async def get_all_posts():
    return POSTS

async def get_post_by_id(id : int):
    post = queryId(POSTS , id)
    return post

async def create_post(new_post : Post):
    new_id : int = len(POSTS)+1 if POSTS else 1
    post_dict : dict = new_post.model_dump()
    post_dict["id"] = new_id
    POSTS.append(post_dict)
    return post_dict