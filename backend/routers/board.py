from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models import Post


# router 객체 등록
router = APIRouter(
    prefix="/api/board",
)


@router.get("/list")
def get_post_list(db: Session = Depends(get_db)):
    _posts = db.query(Post).order_by(Post.created_at.desc()).all()  # 질문 목록 조회
    return _posts
