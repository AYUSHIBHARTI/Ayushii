from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

task_list = []

class Task(BaseModel):
    task: str

@app.get("/tasks")
def view_tasks():
    return task_list if task_list else "No tasks available."

@app.post("/tasks")
def add_task(task: Task):
    task_list.append(task.task)
    return {"message": "Task added!"}

@app.delete("/tasks/{index}")
def delete_task(index: int):
    try:
        task_list.pop(index)
        return {"message": "Task deleted!"}
    except IndexError:
        return {"message": "Task not found."}

