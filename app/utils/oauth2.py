import jwt
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

#SECRET_KEY
#ALGORITHM
#EXPIRATION_TIME

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # app/
ENV_PATH = os.path.join(BASE_DIR, '.env')
load_dotenv(ENV_PATH, override=True)


SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY not found in environment variables")

ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRATION_MINUTES = 30    

def create_access_token(data : dict):
    to_encode = data.copy()
    expire = datetime.now() +timedelta(minutes=ACCESS_TOKEN_EXPIRATION_MINUTES)
    to_encode.update({'exp' : expire})

    encoded_jwt = jwt.encode(payload=to_encode,key=SECRET_KEY , algorithm=ALGORITHM) # type: ignore
    return encoded_jwt
