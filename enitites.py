from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class GodSlaveModel(Base):
    __tablename__ = "godSlave"
    id = Column(Integer, primary_key=True, index=True)
    login = Column(String)
    password = Column(String)
    position = Column(String)
    fullname = Column(String)
    photo_URL = Column(String)
    ifTrockist = Column(Boolean)