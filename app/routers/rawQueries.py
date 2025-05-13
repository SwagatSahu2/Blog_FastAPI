from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from ..database import get_db
from utils.sql_loader import load_queries

router = APIRouter(tags=["raw-sql"])

queries = load_queries()

@router.get('/raw/blog-titles')
def get_blog_titles_raw(db: Session = Depends(get_db)):
    try:
        query = text(queries["get_blog_titles"])
        result = db.execute(query)
        titles = [row[0] for row in result]
        if not titles:
            raise HTTPException(status_code=404, detail="No blog titles found")
        return {"titles": titles}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@router.get('/raw/blog-fields')
def get_blog_fields_raw(attribute: str, db: Session = Depends(get_db)):
    try:
        query = text(queries["get_blog_fields"].format(attribute=attribute))
        result = db.execute(query)
        fields = [row[0] for row in result]
        if not fields:
            raise HTTPException(status_code=404, detail=f"No data found for attribute '{attribute}'")
        return {"fields": fields}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@router.get('/raw/blog-creator')
def get_blog_creator_raw(blog_id: int, db: Session = Depends(get_db)):
    try:
        query = text(queries["get_blog_creator"])
        result = db.execute(query, {"blog_id": blog_id}).fetchone()
        if not result:
            raise HTTPException(status_code=404, detail=f"Creator for blog ID {blog_id} not found")
        return {"name": result.creator_name, "email": result.creator_email}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@router.get('/raw/blogs')
def get_blog_by_user(user_id: int, db: Session = Depends(get_db)):
    try:
        query = text(queries["get_blogs_by_user"])
        results = db.execute(query, {"user_id": user_id}).fetchall()
        if not results:
            raise HTTPException(status_code=404, detail=f"No blogs found for user ID {user_id}")
        return [{"title": row.title, "body": row.body} for row in results]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")