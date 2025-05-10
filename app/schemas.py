from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    title: str
    body: str
    user_id: int

    class Config():
        orm_mode = True

class NewBlog(BaseModel):
    title: str
    body: str

    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str

    class Config():
        orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: Optional[ShowUser]

    class Config():
        orm_mode = True
