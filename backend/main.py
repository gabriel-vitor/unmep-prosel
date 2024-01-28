from fastapi import FastAPI
import uvicorn 

app = FastAPI()

@app.get("/")
def root():
    return{"message": "Hello, world!"}

from fastapi import FastAPI, HTTPException
from models import Task

app = FastAPI()

@app.get("/tasks")
def get_tasks():
    tasks = Task.query.all()
    return tasks

@app.post("/tasks")
def create_task(task: Task):
    task.save()
    return task

@app.put("/tasks/{id}")
def update_task(id: int, task: Task):
    task_to_update = Task.query.get(id)
    if task_to_update is None:
        raise HTTPException(status_code=404, detail="Task not found")
    task_to_update.title = task.title
    task_to_update.description = task.description
    task_to_update.date = task.date
    task_to_update.status = task.status
    task_to_update.save()
    return task_to_update

@app.delete("/tasks/{id}")
def delete_task(id: int):
    task_to_delete = Task.query.get(id)
    if task_to_delete is None:
        raise HTTPException(status_code=404, detail="Task not found")
    task_to_delete.delete()
    return {"message": "Task deleted"}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)