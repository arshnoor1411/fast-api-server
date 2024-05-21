import schemas
from database import models

import bcrypt
from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from database.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func
from fastapi import Depends, FastAPI, HTTPException


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
    print("User",user)
    existing_user = db.query(models.User).filter_by(email = user.email).first

    if existing_user:
        raise HTTPException(status_code=400, detail="Email Already Registered")
    
    hashPassword = bcrypt.hashpw(user.password, bcrypt.gensalt())

    new_user = models.User(firstname = user.firstname,lastname = user.lastname, email = user.email, password = hashPassword, createdAt = func.now(), updatedAt = func.now(), deletedAt = func.now())

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return {"message":"User Created Successfully"}

@router.get("/get")
def getWorld():
    return "Hello World"