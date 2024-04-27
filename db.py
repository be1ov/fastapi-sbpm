from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://sbpm:vv7Qs16L3jos@us-server.be1ov.ru:54320/SBPMApplication"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()