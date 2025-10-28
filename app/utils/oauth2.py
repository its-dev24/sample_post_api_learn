import jwt
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from fastapi import HTTPException, status, Depends
from app.schema.tokenSchema import TokenData
from fastapi.security import OAuth2PasswordBearer

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
oauth_scheme = OAuth2PasswordBearer(tokenUrl='login')

def create_access_token(data : dict):
    to_encode = data.copy()
    expire = datetime.now() +timedelta(minutes=ACCESS_TOKEN_EXPIRATION_MINUTES)
    to_encode.update({'exp' : expire})

    encoded_jwt = jwt.encode(payload=to_encode,key=SECRET_KEY , algorithm=ALGORITHM) # type: ignore
    return encoded_jwt

def verify_access_token(token : str , credential_exception):
    try: 
        payload = jwt.decode(token, key = SECRET_KEY , ALGORITHM = [ALGORITHM]) # type: ignore
        id : str = payload.get("user_id")
        if id is None:
            raise credential_exception
        token_data = TokenData(id=id)
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = "Token Expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        raise credential_exception
    
    return token_data

def get_current_user(token : str = Depends(oauth_scheme)):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
            detail = "Unablet to verify Credentials",
            headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_access_token(credential_exception=credential_exception , token=token)