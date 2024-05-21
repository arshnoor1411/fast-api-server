from ast import Dict
import os
import jwt 
from datetime import timedelta, datetime

async def sign_jwt(data: dict, expires_delta: timedelta | None = None):
    try:
        ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES')) 
        JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
        ALGORITHM = os.environ.get('ALGORITHM')

        to_encode = data.copy()
        print(to_encode, expires_delta, datetime.now(),timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        if expires_delta:
            expire = datetime.now() + expires_delta
        else:
            expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

        to_encode.update({"exp": expire})

        encoded_jwt = jwt.encode(payload = to_encode, key=JWT_SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    except Exception as e:
        print(e)
