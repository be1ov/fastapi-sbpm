from fastapi import APIRouter

from db import db
from enitites import TaskEntity
from models import Task

router = APIRouter()


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








