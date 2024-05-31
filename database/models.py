import uuid
from sqlalchemy import Column, Integer, String, Date, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID as PGUUID

Base = declarative_base()

target_metadata = Base.metadata

class User(Base):
    __tablename__ = "users"
    id = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    firstname = Column(String, index = True)
    lastname = Column(String, index = True)
    email = Column(String, unique = True, index = True)
    password = Column(String, index = True)
    otp = Column(Integer, index = True)
    createdAt =  Column(Date, server_default = func.now())
    updatedAt =  Column(Date, server_default = func.now(), onupdate = func.now())
    deletedAt =  Column(Date, server_default = func.now())
