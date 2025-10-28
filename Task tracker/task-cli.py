import sys
import os
import json
import datetime


def load_tasks():
    if not os.path.exists("task.json"):
        return []
    
    with open("task.json", "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# add
def add(t):
    tasks = load_tasks()

    if tasks:
        next_id = max(task["id"] for task in tasks) + 1
    else:
        next_id = 1
    
    task = {
        "id": next_id,
        "description": t,
        "status": "false",
        "createdAt": datetime.datetime.now().strftime("%c"),
        "updatedAt": datetime.datetime.now().strftime("%c")
    }

    tasks.append(task)
    with open("task.json", "w") as f:
        json.dump(tasks, f, indent=2)

# update
def update(id, updated_task):
    tasks = load_tasks()
    found = False

    for task in tasks:
        if task["id"] == id:
            task["description"] = updated_task
            task["updatedAt"] = datetime.datetime.now().strftime("%c")
            found = True
            break
    
    if found:
        with open("task.json", "w") as f:
            json.dump(tasks, f, indent=2)
    else:
        print(f"No task found with id: {id}")
    
# delete
def delete(id):
    tasks = load_tasks()
    is_deleted = False

    for i, task in enumerate(tasks):
        if task["id"] == id:
            tasks.pop(i)
            is_deleted = True
            break
    
    if is_deleted:
        with open("task.json", "w") as f:
            json.dump(tasks, f, indent=2)
    else:
        print(f"No task found with id: {id}")

# mark-in-progress
def mark_in_progress(id):
    tasks = load_tasks()
    found = False

    for task in tasks:
        if task["id"] == id:
            task["status"] = "in-progress"
            found = True
            break
    
    if found:
        with open("task.json", "w") as f:
            json.dump(tasks, f, indent=2)
    else:
        print(f"No task found with id: {id}")
        
    
# mark-done
def mark_done(id):
    tasks = load_tasks()
    found = False

    for task in tasks:
        if task["id"] == id:
            task["status"] = "done"
            found = True
            break
    
    if found:
        with open("task.json", "w") as f:
            json.dump(tasks, f, indent=2)
    else:
        print(f"No task found with id: {id}")
    

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
    elif command == "update":
        id = int(sys.argv[2])
        updated_task = sys.argv[3]

        if id < 0:
            print("provide valid id")
            sys.exit()

        if len(updated_task) == 0:
            print("provide updated task")
            sys.exit()
        
        update(id, updated_task)
    elif command == "delete":
        id = int(sys.argv[2])
        if id < 0:
            print("provide valid id")
            sys.exit()

        delete(id)
    elif command == "mark-in-progress":
        id = int(sys.argv[2])
        if id < 0:
            print("provide valid id")
            sys.exit()

        mark_in_progress(id)
    elif command == "mark-done":
        id = int(sys.argv[2])
        if id < 0:
            print("provide valid id")
            sys.exit()

        mark_done(id)    


