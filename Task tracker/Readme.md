# 📝 Task Tracker CLI

A simple **command-line task tracker** built with **Python**.

This tool lets you **add, update, delete, list, and manage** your daily tasks directly from the terminal.

---

## 🚀 Features

* **Add** new tasks
* **Update** existing tasks
* **Delete** tasks
* **Mark** tasks as **done** or **in-progress**
* **List** tasks by status (**todo**, **in-progress**, **done**)
* Automatically saves tasks to a `task.json` file in the current directory
* Uses only Python’s native modules — **no external libraries!**

---

## 🧩 Requirements

* Python 3.6+
* No extra installations required — uses:
    * `os`
    * `json`
    * `datetime`
    * `shlex`

---

## ⚙️ Setup

1.  Clone or download the project folder.
2.  Open a terminal in the folder where `task-cli.py` is located.
3.  Run the CLI:

    ```bash
    python task-cli.py
    ```

    You’ll see:

    ```
    No task in DB, Create one!
    Enter command:
    ```

    Your task tracker is now ready to use ✅

---

## 💡 Usage

The CLI keeps running until you type `quit` or `exit`.

Below are all supported commands 👇

### ➕ Add a new task

```bash
add "Buy groceries"