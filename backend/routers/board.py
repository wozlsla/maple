from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from backend.database import get_db
from backend.schemas import board_schema
from backend.services import board_service


# router 객체 등록
router = APIRouter(
    prefix="/api/v1/board",
)


@router.get("/list", response_model=board_schema.PostList)
def get_posts(db: Session = Depends(get_db), page: int = 0, size: int = 15):
    total, _post_list = board_service.get_posts(db, skip=page * size, limit=size)
    return {"total": total, "post_list": _post_list}


@router.get("/detail/{post_id}", response_model=board_schema.Post)
def post_detail(post_id: int, db: Session = Depends(get_db)):
    post = board_service.get_post(db, post_id=post_id)
    return post


@router.post("/detail/{post_id}/comment", status_code=status.HTTP_204_NO_CONTENT)
def add_comment(
    post_id: int,
    _add_comment: board_schema.CommentCreate,
    db: Session = Depends(get_db),
):
    post = board_service.get_post(db, post_id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    board_service.create_comment(
        db,
        post=post,
        add_comment=_add_comment,
    )


@router.post("/post", status_code=status.HTTP_204_NO_CONTENT)
def add_post(
    _post_create: board_schema.PostCreate,
    db: Session = Depends(get_db),
):
    board_service.create_post(db=db, post_create=_post_create)
