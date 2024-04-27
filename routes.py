from fastapi import APIRouter

from db import db
from enitites import TaskEntity, TaskStatusEntity
from models import Task, TaskStatus

router = APIRouter()


@router.post("/tasks")
def addTask(task: Task):
    taskModel = TaskEntity(title = task.title, project_id = task.project_id,
                           description = task.description, creator_id = task.creator_id, controller_id = task.controller_id, executor_id = task.executor_id)
    db.add(taskModel)
    db.commit()
    return {"message": task}

@router.get("/tasks/{id}")
def getTaskByID(id: int):
    task = db.get(TaskEntity, id)
    return {"Task": task}

@router.get("/tasks")
def getTasks():
    tasks = db.query(TaskEntity).all()
    return {"Task[]": tasks}

@router.update("/tasks/{id}")
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








@router.post("/task_statuses")
def addTaskStatus(taskStatus: TaskStatus):
    taskStatusModel = TaskStatusEntity(date = taskStatus.date, task_id = taskStatus.task_id,
                           status = taskStatus.status, user_id = taskStatus.user_id, commentary = taskStatus.commentary)
    db.add(taskStatusModel)
    db.commit()
    return {"message": taskStatus}

@router.get("/task_statuses/{id}")
def getTaskStatusByID(id: int):
    task_status = db.get(TaskStatusEntity, id)
    return {"TaskStatus": task_status}

@router.get("/task_statuses")
def getTaskStatuses():
    taskStatuses = db.query(TaskStatusEntity).all()
    return {"TaskStatuses[]": taskStatuses}

@router.update("/task_statuses/{id}")
def updateTaskStatusByID(id: int, taskStatus: TaskStatus):
    taskStatusModel = db.get(TaskStatusEntity, id)
    taskStatusModel.date = taskStatus.date
    taskStatusModel.task_id = taskStatus.task_id
    taskStatusModel.status = taskStatus.status
    taskStatusModel.user_id = taskStatus.user_id
    taskStatusModel.commentary = taskStatus.commentary
    db.commit()
    return {"TaskStatus": taskStatus}

@router.delete("/task_statuses/{id}")
def deleteTaskStatusByID(id: int):
    taskStatus = db.get(TaskStatusEntity, id)
    db.delete(taskStatus)
    db.commit()
    return {"TaskStatus": taskStatus}
