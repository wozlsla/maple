import datetime
from pydantic import BaseModel, field_validator


class CommentCreate(BaseModel):
    content: str

    # content 값이 저장될 때 실행
    @field_validator("content")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return v


class Comment(BaseModel):
    id: int
    content: str
    created_at: datetime.datetime


class PostCreate(BaseModel):
    title: str
    content: str

    @field_validator("title", "content")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return v


class Post(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime.datetime
    comment: list[Comment] = []
