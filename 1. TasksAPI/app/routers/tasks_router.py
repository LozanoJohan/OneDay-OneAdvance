from fastapi import APIRouter, HTTPException, status

from app.models.task_model import Task
from app.data.data_manager import *


router = APIRouter()


@router.get("/users/{user_id}/tasks/{task_id}", response_model=Task)
def read_task(user_id: int, task_id: int):

    users =  get_users()

    user_found = next(filter(lambda user_db: user_db["id"] == user_id, users), None)

    if not user_found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


    task_found = next(filter(lambda task_db: task_db["id"] == task_id, user_found.get("tasks", [])), None)

    if not task_found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    return task_found




@router.get("/users/{user_id}/tasks/", response_model=list[Task])
def read_tasks(user_id: int):

    users =  get_users()

    user_found = next(filter(lambda user_db: user_db["id"] == user_id, users), None)

    if not user_found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return user_found["tasks"]



@router.get("/tasks/")
def read_all_tasks():

    return get_tasks()



@router.patch("/users/{user_id}/tasks/{task_id}", status_code=status.HTTP_202_ACCEPTED)
def set_task_done(user_id: int, task_id: int):

    users =  get_users()

    user_found = next(filter(lambda user_db: user_db["id"] == user_id, users), None)

    if not user_found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    

    task_found = next(filter(lambda task_db: task_db["id"] == task_id, user_found.get("tasks", [])), None)

    if not task_found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    task_found.update({"completion_status": True})

    write_data(users)

    return task_found




@router.post("/users/{user_id}/tasks/", status_code=status.HTTP_201_CREATED)
async def create_task(user_id: int, task: Task):
    
    users =  get_users()

    user_found = next(filter(lambda user_db: user_db["id"] == user_id, users), None)

    if not user_found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    

    task_found = next(filter(lambda task_db: task_db["id"] == task.id, user_found.get("tasks", [])), None)

    if task_found:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Task already exists")
    
    user_found["tasks"].append(task.dict())

    write_data(users)

    return task




@router.delete("/users/{user_id}/tasks/{task_id}")
def delete_task(user_id: int, task_id: int):

    users =  get_users()

    user_found = next(filter(lambda user_db: user_db["id"] == user_id, users), None)

    if not user_found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    

    task_found = next(filter(lambda task_db: task_db["id"] == task_id, user_found.get("tasks", [])), None)

    if not task_found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    user_found["tasks"].remove(task_found)

    write_data(users)

    return {"message": "Task deleted"}



@router.put("/users/{user_id}/tasks/", response_model=Task)
def update_task(user_id: int, task: Task):

    users =  get_users()

    user_found = next(filter(lambda user_db: user_db["id"] == user_id, users), None)

    if not user_found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    

    task_found = next(filter(lambda task_db: task_db["id"] == task.id, user_found.get("tasks", [])), None)

    if not task_found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    task_found.update(task.dict())

    write_data(users)

    return task_found
