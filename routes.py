from db import db
from enitites import TaskEntity
from models import Task

from passlib.context import CryptContext
from fastapi import APIRouter

from enitites import UserEntity
from models import User

router = APIRouter()

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.get("/users", tags=["users"])
async def get_all_users(id: int = None):
    if id is None:
        return db.query(UserEntity).all()
    else:
        return db.get(UserEntity, id)


@router.post("/users/create", tags=["users"])
async def create_user(user: User):
    hashed_password = password_context.hash(user.password)
    new_user = UserEntity(first_name=user.first_name, last_name=user.last_name, email=user.email, password=hashed_password)
    db.db.add(new_user)
    db.db.commit()
    return {"user": user}

@router.post("/task")
def addTask(task: Task):
    taskModel = TaskEntity(title = task.title, project_id = task.project_id,
                           description = task.description, creator_id = task.creator_id, controller_id = task.controller_id, executor_id = task.executor_id)
    db.add(taskModel)
    db.commit()
    return {"message": task}

@router.get("/task/{id}")
def getTaskByID(id: int):
    task = db.get(TaskEntity, id)
    return {"Task": task}

@router.get("/task")
def getTasks():
    tasks = db.query(TaskEntity).all()
    return {"Task[]": tasks}

@router.update("/task/{id}")
def updateTaskByID(id: int, task: Task):
    taskModel = db.get(TaskEntity, id)
    taskModel.title = task.title
    taskModel.project_id = task.project_id
    taskModel.description = task.description
    taskModel.creator_id = task.creator_id
    taskModel.controller_id = task.controller_id
    taskModel.executor_id = task.executor_id
    db.commit()
    return {"Task": task}

@router.delete("/tasks/{id}")
def deleteTaskByID(id: int):
    task = db.get(TaskEntity, id)
    db.delete(task)
    db.commit()
    return {"Task": task}