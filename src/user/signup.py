import schemas
from database import models

import bcrypt
from fastapi import APIRouter, Depends, HTTPException,status
from database.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func
from fastapi import Depends, HTTPException
from sqlalchemy.future import select
from passlib.context import CryptContext
import src.auth.token



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
    
    
@router.get("/login")
async def login(request:schemas.SignInModel, db: AsyncSession = Depends(get_db)):
    try:
        user = await db.execute(select(models.User).filter_by(email = request.email))
        existing_user = user.scalar_one_or_none()
        #  print("USer",existing_user.password)

        if user is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email")
        
        password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        print("Hello")

        verify_user = password_context.verify(request.password, existing_user.password)
        print("Verify",verify_user)

        if not verify_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Incorrect password"
            )
        
        token = await src.auth.token.sign_jwt(data={"sub": str(existing_user.id),"name": str(existing_user.firstname)})

        return token
     
    except Exception as e:
     await db.rollback()
        

@router.get("/get")
def getWorld():
    return "Hello World"