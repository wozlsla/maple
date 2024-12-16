from datetime import datetime
from sqlalchemy.orm import Session

from backend.models import Post, Comment
from backend.schemas.board_schema import CommentCreate, PostCreate


def get_posts(db: Session):
    posts = db.query(Post).order_by(Post.created_at.desc()).all()
    return posts


def get_post(db: Session, post_id: int):
    post = db.query(Post).get(post_id)
    return post


def create_comment(db: Session, post: Post, add_comment: CommentCreate):
    db_comment = Comment(
        post=post,
        content=add_comment.content,
        created_at=datetime.now(),
    )
    db.add(db_comment)
    db.commit()


def create_post(db: Session, post_create: PostCreate):
    db_post = Post(
        title=post_create.title, content=post_create.content, created_at=datetime.now()
    )
    db.add(db_post)
    db.commit()
