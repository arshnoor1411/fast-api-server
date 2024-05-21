import schemas
from database import models

import bcrypt
from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from database.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.future import select


# def get_session():
#     session = SessionLocal()
#     try:
#         yield session
#     finally:
#         session.close()
# app=FastAPI()
# print("App",app)

router = APIRouter()

# app = FastAPI()

@router.post("/signup")
async def signup(user: schemas.SignUpModel, db: AsyncSession = Depends(get_db)):
    try:
        print("User",user)
        existing_user = await db.execute(select(models.User).filter_by(email=user.email))
        print(existing_user)

        # if existing_user:
        #   raise HTTPException(status_code=400, detail="Email already registered")
        
        hashPassword = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
        stringHashPassword = hashPassword.decode('utf-8')

        new_user = models.User(firstname = user.firstname,lastname = user.lastname, email = user.email, password = stringHashPassword, createdAt = func.now(), updatedAt = func.now(), deletedAt = func.now())

        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)

        return {"message":"User Created Successfully"}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail="Email already registered")
        

@router.get("/get")
def getWorld():
    return "Hello World"