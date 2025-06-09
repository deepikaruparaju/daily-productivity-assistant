import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(task, due_time):
    tasks = load_tasks()
    tasks.append({"task": task, "due_time": due_time, "done": False})
    save_tasks(tasks)

def get_all_tasks():
    return load_tasks()

def delete_task_by_index(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)

def update_task_done_status(index, status):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]['done'] = status
        save_tasks(tasks)