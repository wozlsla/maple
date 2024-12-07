from backend.models import Post
from sqlalchemy.orm import Session


def get_post_list(db: Session):
    posts = db.query(Post).order_by(Post.created_at.desc()).all()
    return posts
