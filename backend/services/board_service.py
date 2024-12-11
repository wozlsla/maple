from backend.models import Post
from sqlalchemy.orm import Session


def get_posts(db: Session):
    posts = db.query(Post).order_by(Post.created_at.desc()).all()
    return posts


def get_post(db: Session, post_id: int):
    post = db.query(Post).get(post_id)
    return post
