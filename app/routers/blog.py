from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session  
from ..auth import create_access_token, get_current_user

router = APIRouter()

@router.get('/blog', response_model=List[schemas.ShowBlog], tags=["blogs"])
def get_blogs(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.post('/blog', tags=["blogs"])
def create(request: schemas.NewBlog, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=current_user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get('/blog/{id}', response_model=schemas.ShowBlog, tags=["blogs"])
def get_blog(id: int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} is not available")
    return blog

@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["blogs"])
def remove(id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
                            

    if blog.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete this blog")
                            

    db.delete(blog)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put('/blog/{id}', tags=["blogs"])
def update(id, request: schemas.NewBlog, db : Session= Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete this blog")
    blog.title = request.title
    blog.body = request.body
    db.commit()
    return 'updated'