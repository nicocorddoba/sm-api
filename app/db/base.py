from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

from dotenv import load_dotenv
import os 

Base = declarative_base()

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()