from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db
from ..auth import get_current_user

router = APIRouter(tags=["comments"])

@router.post('/blogs/{blog_id}/comments', response_model=schemas.Comment)
def create_comment(
    blog_id: int,
    request: schemas.CommentBase,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user)
):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    new_comment = models.Comment(body=request.body, blog_id=blog_id, user_id=current_user.id)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

@router.get('/blogs/{blog_id}/comments', response_model=List[schemas.Comment])
def get_comments(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail=f"Blog with ID {blog_id} not found")
    
    comments = db.query(models.Comment).filter(models.Comment.blog_id == blog_id).all()
    if not comments:
        raise HTTPException(status_code=404, detail=f"No comments found for Blog ID {blog_id}")
    
    return comments

@router.delete('/comments/{comment_id}', status_code=204)
def delete_comment(
    comment_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user)
):
    comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    
    if comment.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this comment")
    
    db.delete(comment)
    db.commit()