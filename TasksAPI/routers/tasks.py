from typing import Dict
from fastapi import APIRouter, HTTPException, status
from models.task import Task
import json

with open("./data/tasks_fake_db.json", "r+") as file:
    tasks: list[Dict] = json.load(file)

router = APIRouter()


@router.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):

    tasks_found = filter(lambda task: task["id"] == task_id, tasks)

    try:
        task_found = list(tasks_found)[0] 
        return task_found
    
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")




@router.get("/tasks/", response_model=list[Task])
def read_tasks():

    return tasks




@router.get("/tasks/name/{name}", response_model=list[Task])
def read_task_by_name(name: str):

    tasks_found = filter(lambda task: task["name"] == name, tasks)

    return list(tasks_found)




@router.patch("/tasks/{task_id}", status_code=status.HTTP_202_ACCEPTED)
def set_task_done(task_id: int):

    tasks_found = filter(lambda task: task["id"] == task_id, tasks)

    try:
        task_found: dict = list(tasks_found)[0]
        task_found.update({"completion_status": True})

        with open("./data/tasks_fake_db.json", "w") as file:
            json.dump(tasks, file, indent=4)

        return task_found

    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")




@router.post("/tasks/", status_code=status.HTTP_201_CREATED)
async def create_task(task: Task):
    
    tasks_found = filter(lambda task_db: task_db["id"] == task.id, tasks)

    if len(list(tasks_found)) > 0:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Task already exists")
    
    tasks.append(task.dict())

    with open("./data/tasks_fake_db.json", "w") as file:
        json.dump(tasks, file, indent=4)

    return tasks[-1]




@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    tasks_found = filter(lambda task: task["id"] == task_id, tasks)

    try:
        task_found = list(tasks_found)[0]

        tasks.remove(task_found)

        with open("./data/tasks_fake_db.json", "w") as file:
            json.dump(tasks, file, indent=4)

        return task_found
    
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")




@router.put("/tasks/", response_model=Task)
def update_task(task: Task):

    tasks_found = filter(lambda task_db: task_db["id"] == task.id, tasks)

    try:
        task_found = list(tasks_found)[0]

        task_found.update(task.dict())
    
        with open("./data/tasks_fake_db.json", "w") as file:
            json.dump(tasks, file, indent=4)
        
        return task_found
    
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

