from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from ..database import get_db

router = APIRouter(tags=["raw-sql"])

@router.get('/raw/blog-titles')
def get_blog_titles_raw(db: Session = Depends(get_db)):
    query = text("SELECT title FROM blogs")
    result = db.execute(query)
    titles = [row[0] for row in result]
    return {"titles": titles}

@router.get('/raw/blog-fields')
def get_blog_fields_raw(variable: str, db: Session = Depends(get_db)):
    query = text(f"SELECT {variable} FROM blogs")
    result = db.execute(query)
    fields = [row[0] for row in result]
    return {"fields": fields}

@router.get('/raw/blog-creator')
def get_blog_creator_raw(blog_id: int, db: Session = Depends(get_db)):
    query = text("""
        SELECT 
            users.name AS creator_name, 
            users.email AS creator_email
        FROM blogs
        JOIN users ON blogs.user_id = users.id
        WHERE blogs.id = :blog_id
    """)
    result = db.execute(query, {"blog_id": blog_id}).fetchone()

    if not result:
        raise HTTPException(status_code=404, detail=f"Creator for blog ID {blog_id} not found")

    return {
        "name": result.creator_name,
        "email": result.creator_email
    }

@router.get('/raw/blogs')
def get_blog_by_user(user_id: int, db: Session = Depends(get_db)):
    query = text("SELECT blogs.title, blogs.body FROM blogs WHERE user_id = :user_id")
    results = db.execute(query, {"user_id": user_id}).fetchall()
    return [{"title": row.title, "body": row.body} for row in results]

# @router.get('/raw/blog/{id}/creator', tags=["raw-sql"])
# def get_blog_creator_raw(id: int, db: Session = Depends(get_db)):
#     query = text("""
#         SELECT 
#             users.name AS creator_name, 
#             users.email AS creator_email
#         FROM blogs
#         JOIN users ON blogs.user_id = users.id
#         WHERE blogs.id = :blog_id
#     """)
#     result = db.execute(query, {"blog_id": id}).fetchone()

#     if not result:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Creator for blog ID {id} not found")

#     return {
#         "name": result.creator_name,
#         "email": result.creator_email
#     }