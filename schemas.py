from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class SignUpModel(BaseModel):
    id: UUID
    firstname: str
    lastname: str
    email: str
    password: str
    createdAt: datetime
    updatedAt: datetime
    deletedAt: datetime