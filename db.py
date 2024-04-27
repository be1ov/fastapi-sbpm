from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "Host=us-server.be1ov.ru;Port=54320;Database=SBPMApplication;Username=sbpm;Password=vv7Qs16L3jos"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()




class TroykaModel(Base):
    __tablename__ = "troyka"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    gebist_id = Column(Integer, ForeignKey("godSlave.id"))
    commy_id = Column(Integer, ForeignKey("godSlave.id"))
    prokuror_id = Column(Integer, ForeignKey("godSlave.id"))


class SentenceModel(Base):
    __tablename__ = "sentence"
    id = Column(Integer, primary_key=True, index=True)
    troyka_id = Column(Integer, ForeignKey("troyka.id"))
    description = Column(String)
    ifExecution = Column(Boolean)


class PolitburoModel(Base):
    __tablename__ = "politburo"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)


Base.metadata.create_all(bind=engine)
