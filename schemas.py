from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class SignUpModel(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str

class SignUp(SignUpModel):
    id: UUID
    createdAt: datetime
    updatedAt: datetime
    deletedAt: datetime
