import datetime

from pydantic import BaseModel


class Post(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime.datetime
