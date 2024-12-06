from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# DB 접속 주소
SQLALCHEMY_DATABASE_URL = "sqlite:///./maple.db"

# ConnectionPool 생성
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# DB 세션 생성 (접속)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()  # db session 객체 생성
    try:
        yield db
    finally:
        db.close()  # session 반환 (컨넥션 풀에 반환 / 종료 X)
