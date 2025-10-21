#SQL alchemy code

from sqlalchemy import create_engine,Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # app/
ENV_PATH = os.path.join(BASE_DIR, '.env')
load_dotenv(ENV_PATH, override=True)

SQL_ALCHEMY_DB_URL = f"postgresql://{os.getenv('USERNAME')}:{os.getenv('PASSWORD')}@localhost/{os.getenv('DATABASE')}"

engine : Engine = create_engine(SQL_ALCHEMY_DB_URL)

SessionLocal = sessionmaker(autocommit = False , autoflush= False , bind = engine)

Base = declarative_base() 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()