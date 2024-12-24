from database import Base
from sqlalchemy import Column,Integer,String,Boolean
class User(Base):
    __tablename__="users"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(32),nullable=False)
    email = Column(String,unique=True,nullable=False)
    is_active = Column(Boolean )  
