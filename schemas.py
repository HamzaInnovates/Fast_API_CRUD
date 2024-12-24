from pydantic import BaseModel

class UserSchema(BaseModel):
    id:int
    name:str
    email:str
    is_active:bool
    class Config:
        orm_mode=True