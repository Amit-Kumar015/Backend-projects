import os
import json
import datetime
import shlex

# get all tasks
def load_tasks():
    if not os.path.exists("task.json"):
        return []
    
    with open("task.json", "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# show tasks
def show_tasks():
    tasks = load_tasks()

    print(f"{'ID':<5} {'Description':<30} {'Status':<12}")
    print("-" * 50)

    for task in tasks:
        print(f"{task['id']:<5} {task['description']:<30} {task['status']:<12}")


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
        "status": "todo",
        "createdAt": datetime.datetime.now().strftime("%c"),
        "updatedAt": datetime.datetime.now().strftime("%c")
    }

    tasks.append(task)
    with open("task.json", "w") as f:
        json.dump(tasks, f, indent=2)
    show_tasks()

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
        show_tasks()
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
        show_tasks()
    else:
        print(f"No task found with id: {id}")

# mark-in-progress
def mark_in_progress(id):
    tasks = load_tasks()
    found = False

    for task in tasks:
        if task["id"] == id:
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.datetime.now().strftime("%c")
            found = True
            break
    
    if found:
        with open("task.json", "w") as f:
            json.dump(tasks, f, indent=2)
        show_tasks()
    else:
        print(f"No task found with id: {id}")
        
    
# mark-done
def mark_done(id):
    tasks = load_tasks()
    found = False

    for task in tasks:
        if task["id"] == id:
            task["status"] = "done"
            task["updatedAt"] = datetime.datetime.now().strftime("%c")
            found = True
            break
    
    if found:
        with open("task.json", "w") as f:
            json.dump(tasks, f, indent=2)
        show_tasks()
    else:
        print(f"No task found with id: {id}")


# Listing tasks by status
def list_status(status):
    tasks = load_tasks()
    print(f"{'ID':<5} {'Description':<30} {'Status':<12}")
    print("-" * 50)

    for task in tasks:
        if task["status"] == status:
            print(f"{task['id']:<5} {task['description']:<30} {task['status']:<12}")
    


once = True
while True:
    tasks = load_tasks()

    if once:
        if len(tasks) == 0:
            print("No task in DB, Create one!")
        else:
            show_tasks()
        once = False

    command = input("Enter command: ")
    parts = shlex.split(command)

    cmd = parts[0]
    argv = len(parts)

    if cmd == "add":
        if argv != 2:
            print("Please provide correct command")
            continue
        
        task = parts[1]
        add(task)
    elif cmd == "update":
        if argv != 3:
            print("Please provide correct command")
            continue
        
        id = int(parts[1])
        if id < 0:
            print("provide valid id")
            continue

        updated_task = parts[2]
        if len(updated_task) == 0:
            print("provide updated task")
            continue
        
        update(id, updated_task)
    elif cmd == "delete":
        if argv != 2:
            print("Please provide correct command")
            continue
        
        if parts[1].isdigit():
            id = int(parts[1])
            if id < 0:
                print("provide valid id")
                continue
        else:
            print("Please provide a valid integer ID.")
        
        delete(id)
    elif cmd == "mark-in-progress":
        if argv != 2:
            print("Please provide correct command")
            continue
        
        if parts[1].isdigit():
            id = int(parts[1])
            if id < 0:
                print("provide valid id")
                continue
        else:
            print("Please provide a valid integer ID.")
        
        mark_in_progress(id)
    elif cmd == "mark-done":
        if argv != 2:
            print("Please provide correct command")
            continue
        
        if parts[1].isdigit():
            id = int(parts[1])
            if id < 0:
                print("provide valid id")
                continue
        else:
            print("Please provide a valid integer ID.")
        
        mark_done(id)
    elif cmd == "list":
        if argv == 2:
            status = parts[1]
            if status not in ["done", "todo", "in-progress"]:
                print("provide valid status")
            else:
                list_status(status)
        elif argv > 2:
            print("Please provide correct command")
        else:
            show_tasks()
    elif cmd == "quit" or cmd == "exit" or cmd == "break":
        break

            

