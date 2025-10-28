import sys
import os
import json

def load_tasks():
    if not os.path.exists("task.json"):
        return []
    
    with open("task.json", "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def add(t):
    tasks = load_tasks()

    if tasks:
        next_id = max(task["id"] for task in tasks) + 1
    else:
        next_id = 1
    
    task = {
        "id": next_id,
        "task": t,
        "done": "false"
    }

    tasks.append(task)
    with open("task.json", "w") as f:
        json.dump(tasks, f)



if len(sys.argv) < 2:
    print("Please provide a command")
else:
    command = sys.argv[1]

    if command == "add":
        task = sys.argv[2]
        if len(task) == 0:
            print("Please provide a task")
        else:
            add(task)



