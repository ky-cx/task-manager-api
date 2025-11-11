"""
Simple Task Manager API
A RESTful API built with FastAPI for managing tasks
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="Task Manager API", version="1.0.0")

# In-memory database (for demo purposes)
tasks_db = []
task_id_counter = 1


class Task(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TaskResponse(Task):
    id: int
    created_at: datetime


@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {
        "message": "Welcome to Task Manager API",
        "endpoints": {
            "GET /tasks": "Get all tasks",
            "POST /tasks": "Create a new task",
            "GET /tasks/{id}": "Get a specific task",
            "PUT /tasks/{id}": "Update a task",
            "DELETE /tasks/{id}": "Delete a task"
        }
    }


@app.get("/tasks", response_model=List[TaskResponse])
def get_tasks(completed: Optional[bool] = None):
    """Get all tasks, optionally filter by completion status"""
    if completed is None:
        return tasks_db
    return [task for task in tasks_db if task["completed"] == completed]


@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: Task):
    """Create a new task"""
    global task_id_counter
    new_task = {
        "id": task_id_counter,
        "title": task.title,
        "description": task.description,
        "completed": task.completed,
        "created_at": datetime.now()
    }
    tasks_db.append(new_task)
    task_id_counter += 1
    return new_task


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    """Get a specific task by ID"""
    task = next((task for task in tasks_db if task["id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: Task):
    """Update an existing task"""
    task = next((task for task in tasks_db if task["id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task["title"] = task_update.title
    task["description"] = task_update.description
    task["completed"] = task_update.completed
    return task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    """Delete a task"""
    global tasks_db
    task = next((task for task in tasks_db if task["id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    tasks_db = [task for task in tasks_db if task["id"] != task_id]
    return None


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
