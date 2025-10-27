# from app.DB import POSTS
from app.utils import queryId
import app.schema as Schema
from app.DB import conn,get_cursor
from app.model import Post
from sqlalchemy.orm import Session

cursor = get_cursor()

async def get_all_posts(db):  
    # cursor.execute("""SELECT * FROM posts""")
    # all_posts  = cursor.fetchall()

    all_posts = db.query(Post).all()
    return all_posts

async def get_post_by_id(id : int, db : Session):
    
    #sql alchemy
    post = db.query(Post).filter(Post.id == id).first()
    return post
    
    #psycopg2
    # cursor.execute("""SELECT * FROM posts WHERE id =%s""" , (str(id)))
    # post = cursor.fetchone()

    #in - memory
    # idx,post = queryId(POSTS , id)
    # return post
    return 1

async def create_post(new_post :  Schema.createPost, db : Session):

    #in memory

    # new_id : int = len(POSTS)+1 if POSTS else 1
    # post_dict : dict = new_post.model_dump()
    # post_dict["id"] = new_id
    # POSTS.append(post_dict)

    #psycopg2

    # cursor.execute("""INSERT INTO posts (title , content , published) VALUES (%s,%s,%s) RETURNING * ;""", (new_post.title , new_post.content , new_post.published))
    # inserted_post = cursor.fetchone()
    # conn.commit()
    # return inserted_post


    #sql-alchemy
    
    post  = Post(**new_post.model_dump())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

async def update_single_post(id : int , updated_post : Schema.UpdatePost,db : Session):
     
    #sql-alchemy
    post_query = db.query(Post).filter(Post.id == id)
    post = post_query.first()

    if post == None:
         return None
    post_query.update(updated_post.model_dump(exclude_unset=True),synchronize_session=False) # type: ignore
    db.commit()
    db.refresh(post)
    return post
#     # idx,post = queryId(POSTS,id)
#     cursor.execute("""UPDATE posts SET title = %s , content = %s , published = %s WHERE id = %s RETURNING * ;""" , (updated_post.title , updated_post.content , updated_post.published , id))
#     post = cursor.fetchone()
#     conn.commit()
#     # if post is not None:
#         # updated_data = updated_post.model_dump(exclude_unset=True)
#         # POSTS[post.get("id")] = post.model_copy(update = updated_data)
#         # POSTS[idx] = {**post , **updated_data}
#         # return post
#     return post

async def delete_post(id : int , db : Session):

      #sql-alchemy

        post = db.query(Post).filter(Post.id == id).first()
        if post is None:
             return None
        db.delete(post)
        db.commit()
        return post
        

#     # idx , post = queryId(POSTS,id)
#     # if post is None:
#     #     return None
#     # POSTS.pop(idx)
#     cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * ;""" , (str(id)))
#     post = cursor.fetchone()
#     conn.commit()
#     return post