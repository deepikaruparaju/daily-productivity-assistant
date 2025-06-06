import json
import os

TASK_FILE = "tasks.json"

def init_task_file():
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, "w") as f:
            json.dump([], f)
    else:
        with open(TASK_FILE, "r") as f:
            try:
                data = json.load(f)
                if data and isinstance(data[0], str):
                    migrated = [{"text": task, "done": False} for task in data]
                    save_tasks(migrated)
            except json.JSONDecodeError:
                save_tasks([])

def load_tasks():
    with open(TASK_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(task):
    with open(TASK_FILE, "r") as file:
        tasks = json.load(file)
    tasks.append({"task": task, "done": False})  # 👈 correct format
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)
    return "✅ Task added!"



def view_tasks():
    with open(TASK_FILE, "r") as file:
        tasks = json.load(file)

    display = []
    for i, task in enumerate(tasks):
        status = "✅" if task["done"] else "❌"
        display.append(f"{status} {task['task']}")
    return display  # 👈 Return a list of strings instead of one string


def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        return f"🗑️ Task deleted: {removed['text']}"
    else:
        return "⚠️ Invalid task number."

def toggle_task_status(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = not tasks[index]["done"]
        save_tasks(tasks)
        new_status = "✅ Done" if tasks[index]["done"] else "❌ Not Done"
        return f"🔁 Toggled status: {tasks[index]['text']} → {new_status}"
    else:
        return "⚠️ Invalid task number."
