from typing import Dict
from fastapi import FastAPI
from models.task import Task
import json

with open("./data/fake_db.json", "r+") as file:
    tasks = json.load(file)

app = FastAPI()

@app.get("/")
def read_root():
    return 'Welcome to my awesome TODO api 😎'

@app.get("/tasks/{task_id}")
def read_task(task_id: int):

    tasks_found = filter(lambda task: task["id"] == task_id, tasks)
    task_found = list(tasks_found)[0]

    return task_found

@app.get("/tasks/")
def read_tasks():

    return tasks

@app.get("/tasks/name/{name}")
def read_task_by_name(name: str):

    tasks_found = filter(lambda task: task["name"] == name, tasks)

    return list(tasks_found)

@app.patch("/tasks/{task_id}")
def set_task_done(task_id: int):

    tasks_found = filter(lambda task: task["id"] == task_id, tasks)
    task_found: dict = list(tasks_found)[0]

    task_found.update({"completion_status": True})

    with open("./data/fake_db.json", "w") as file:
        json.dump(tasks, file, indent=4)

    return task_found

@app.post("/tasks/")
async def create_task(task: Task):

    tasks.append(task.dict())
    print(tasks)

    return tasks[-1]

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks_found = filter(lambda task: task["id"] == task_id, tasks)
    task_found = list(tasks_found)[0]

    tasks.remove(task_found)

    with open("./data/fake_db.json", "w") as file:
        json.dump(tasks, file, indent=4)

    return task_found

@app.patch("tasks/{task_id}")
def update_task(task_id: int, task: Task):
 ...

# TODO: See undone
# TODO: Auth users
# TODO: Query by user
# TODO: MongoDB
    

