from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base

import db

Base = declarative_base()


class UserEntity(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)


class ProjectEntity(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)


class TasksEntity(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    description = Column(String)
    creator_id = Column(Integer, ForeignKey("users.id"))
    controller_id = Column(Integer, ForeignKey("users.id"))
    executor_id = Column(Integer, ForeignKey("users.id"))


class TasksStatusesEntity(Base):
    __tablename__ = "task_statuses"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    commentary = Column(String)


Base.metadata.create_all(bind=db.engine)
