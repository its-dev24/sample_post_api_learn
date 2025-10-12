import psycopg2
from dotenv import load_dotenv
import os
from psycopg2.extras import RealDictCursor
import time

def connect_db():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # app/
    ENV_PATH = os.path.join(BASE_DIR, '.env')
    load_dotenv(ENV_PATH, override=True)
    # print(ENV_PATH)
    # print(os.os.getenv('USERNAME'))
    # host = os.getenv('HOST')
    # database = os.getenv('DATABASE')
    # username = os.getenv('USERNAME')
    # password = os.getenv('PASSWORD')
    # port = os.getenv('DB_POST')
    while True : 
        try :
            con = psycopg2.connect(host = os.getenv('HOST') , database = os.getenv('DATABASE') , user = os.getenv('USERNAME') , password = os.getenv('PASSWORD') , port = os.getenv('DB_PORT') , cursor_factory = RealDictCursor)
            print("Connection Succesfull")
            break
        except Exception as error:
            print(f"Database connection error : {error}")
            time.sleep(2)

    return con.cursor()
POSTS = [
    {
        "id": 1,
        "title": "Title of post 1",
        "content": "Content of post 1",
        "published": True,
        "rating": 5,
    },
    {
        "id": 2,
        "title": "Learning FastAPI",
        "content": "FastAPI makes it easy to build APIs quickly with Python.",
        "published": True,
        "rating": 4,
    },
    {
        "id": 3,
        "title": "Intro to Docker",
        "content": "Docker helps package applications into containers for consistency.",
        "published": False,
        "rating": 5,
    },
    {
        "id": 4,
        "title": "Postgres Basics",
        "content": "Postgres is a powerful open-source relational database system.",
        "published": True,
        "rating": 3,
    },
    {
        "id": 5,
        "title": "AWS for Beginners",
        "content": "AWS provides cloud services that scale with your applications.",
        "published": True,
        "rating": 4,
    },
]
