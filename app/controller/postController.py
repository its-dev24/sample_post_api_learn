from app.DB import POSTS
from app.utils import queryId
from app.model import Post,UpdatePost
from app.DB import conn,get_cursor

cursor = get_cursor()

async def get_all_posts():  
    cursor.execute("""SELECT * FROM posts""")
    all_posts  = cursor.fetchall()
    return all_posts

async def get_post_by_id(id : int):
    cursor.execute("""SELECT * FROM posts WHERE id =%s""" , (str(id)))
    post = cursor.fetchone()
    # idx,post = queryId(POSTS , id)
    return post

async def create_post(new_post : Post):
    # new_id : int = len(POSTS)+1 if POSTS else 1
    # post_dict : dict = new_post.model_dump()
    # post_dict["id"] = new_id
    # POSTS.append(post_dict)
    cursor.execute("""INSERT INTO posts (title , content , published) VALUES (%s,%s,%s) RETURNING * ;""", (new_post.title , new_post.content , new_post.published))
    inserted_post = cursor.fetchone()
    conn.commit()
    return inserted_post

async def update_single_post(id : int , updated_post : UpdatePost):
    # idx,post = queryId(POSTS,id)
    cursor.execute("""UPDATE posts SET title = %s , content = %s , published = %s WHERE id = %s RETURNING * ;""" , (updated_post.title , updated_post.content , updated_post.published , id))
    post = cursor.fetchone()
    conn.commit()
    # if post is not None:
        # updated_data = updated_post.model_dump(exclude_unset=True)
        # POSTS[post.get("id")] = post.model_copy(update = updated_data)
        # POSTS[idx] = {**post , **updated_data}
        # return post
    return post

async def delete_post(id : int):
    # idx , post = queryId(POSTS,id)
    # if post is None:
    #     return None
    # POSTS.pop(idx)
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * ;""" , (str(id)))
    post = cursor.fetchone()
    conn.commit()
    return post