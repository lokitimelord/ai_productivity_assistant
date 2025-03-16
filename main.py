from fastapi import FastAPI, Depends, HTTPException
from database import get_db, Task
from sqlalchemy.orm import Session

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    print("Root endpoint accessed!")  # Debugging line
    return {"message": "AI Productivity Assistant is running!"}

# Endpoint to get all tasks
@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return {"tasks": tasks}

# Endpoint to add a task
@app.post("/tasks")
def add_task(task_name: str, db: Session = Depends(get_db)):
    new_task = Task(name=task_name)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"message": f"Task '{task_name}' added successfully!"}

# Endpoint to delete a task by ID
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": f"Task '{task.name}' deleted successfully!"}
