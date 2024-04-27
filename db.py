from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean

SQLALCHEMY_DATABASE_URL = "Host=us-server.be1ov.ru;Port=54320;Database=SBPMApplication;Username=sbpm;Password=vv7Qs16L3jos"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()



Base.metadata.create_all(bind=engine)
