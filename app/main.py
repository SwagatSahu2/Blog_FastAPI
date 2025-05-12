from fastapi import FastAPI, Depends, HTTPException, status, Response
from . import schemas, models, hashing
from .database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from typing import List
from fastapi.security import OAuth2PasswordRequestForm
from .auth import create_access_token, get_current_user
from sqlalchemy import text
from .routers import blog, user, rawQueries, login, comments


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(login.router)
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(rawQueries.router)
app.include_router(comments.router)
