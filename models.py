from pydantic import BaseModel
import datetime


class Task(BaseModel):
    title: str
    project_id: int
    description: str
    creator_id: int
    controller_id: int
    executor_id: int
class TaskStatuses(BaseModel):
    date: datetime
    task_id: int
    status: int
    user_id: int
    commentary: str