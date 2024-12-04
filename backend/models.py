from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base
from datetime import datetime, timezone


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"), nullable=False)

    post = relationship("Post", backref="comment")


# 나중에 추가할 모델
# class User(Base):
#     __tablename__ = "user"

#     id = Column(Integer, primary_key=True)
#     username = Column(String(150), nullable=False, unique=True)
#     password = Column(String, nullable=False)
#     email = Column(String(150), nullable=False, unique=True)
#     created_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)

#     # 관계 설정 (uselist -> 1:1 관계. 한 명의 User당 하나의 Profile) & 모델 참조/역참조 가능
#     profile = relationship("Profile", back_populates="user", uselist=False)


# class Profile(Base):
#     __tablename__ = "profile"

#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
#     bio = Column(Text)
#     avatar_url = Column(String)
#     updated_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)

#     user = relationship("User", back_populates="profile")
