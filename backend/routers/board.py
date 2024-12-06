from fastapi import APIRouter

from backend.database import SessionLocal
from backend.models import Post


# router 객체 등록
router = APIRouter(
    prefix="/api/board",
)


@router.get("/list")
def get_post_list():
    db = SessionLocal()  # db session 생성
    _posts = db.query(Post).order_by(Post.created_at.desc()).all()  # 질문 목록 조회
    db.close()  # session 반환 (컨넥션 풀에 반환 / 종료 X)
    return _posts
