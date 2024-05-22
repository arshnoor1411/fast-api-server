import os
import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_db
from sqlalchemy.future import select
import database.models

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES')) 
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
ALGORITHM = os.environ.get('ALGORITHM')

def decode_token(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    
    except jwt.PyJWTError:
        raise HTTPException(status_code=403, detail="Could not validate credentials")

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    payload = decode_token(token)

    print("Payload",payload)
    email: str = payload.get("sub")
    print(email)

    if email is None:
        raise HTTPException(status_code=403, detail="Could not validate credentials")
    
    result = await db.execute(select(database.models.User).filter_by(email=email))
    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(status_code=403, detail="Could not validate credentials")
    return user