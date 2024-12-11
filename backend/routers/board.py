from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import get_db
from backend import schemas
from backend.services import board_service


# router 객체 등록
router = APIRouter(
    prefix="/api/board",
)


@router.get("/list", response_model=list[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    _posts = board_service.get_posts(db)
    return _posts


@router.get("/detail/{post_id}", response_model=schemas.Post)
def post_detail(post_id: int, db: Session = Depends(get_db)):
    post = board_service.get_post(db, post_id=post_id)
    return post
