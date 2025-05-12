from fastapi import APIRouter, Depends, HTTPException
from typing import List
from .. import schemas, database, models, hashing
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get('/user', response_model = List[schemas.ShowUser], tags=["users"])
def get_users(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return users

@router.post('/user', tags=["users"])
def create_user(request: schemas.User, db: Session=Depends(database.get_db)):
    new_user = models.User(name=request.name, email=request.email, password= hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/user/{id}', response_model=schemas.ShowUser, tags=["users"])
def get_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with ID {id} not found")
    return user