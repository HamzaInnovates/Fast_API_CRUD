from fastapi import FastAPI,Depends,HTTPException
from database import engine,sessionLocal,Base,get_db
from models import User
from schemas import UserSchema
from sqlalchemy.orm import Session

app = FastAPI()
Base.metadata.create_all(bind=engine)
@app.post("/user",response_model=UserSchema)
def add_user(user:UserSchema,db:Session = Depends(get_db)):
    u =User(name=user.name,email=user.email,is_active=user.is_active)
    db.add(u)
    db.commit()
    return u

@app.get('/user',response_model=list[UserSchema])
def get_users(db:Session=Depends(get_db)):
    return db.query(User).all()
@app.get('/user/{id}',response_model=UserSchema)
def get_users(id:int,db:Session=Depends(get_db)):
    return db.query(User).filter(User.id==id)

@app.put('/user/{id}', response_model=UserSchema)
def update_users(user: UserSchema, id: int, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.id == id).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    existing_user.name = user.name
    existing_user.email = user.email
    existing_user.is_active = user.is_active
    db.commit()
    db.refresh(existing_user)
    return existing_user

@app.delete('/user/{id}', response_model=dict)
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return {"detail": "User deleted successfully"}

