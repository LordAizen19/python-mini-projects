# ─────────────────────────────────────────────
#  IMPORTS  (built-in Python modules only)
# ─────────────────────────────────────────────

import sys
import os 
from datetime import datetime
import json

# ─────────────────────────────────────────────
#  CONSTANT
#  One place to store the filename.
#  If you ever want to rename the file, change it here only.
# ─────────────────────────────────────────────

TASKS_FILE = 'tasks.json'

# ─────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────

def load_tasks():
    # If the file doesn't exist , then return the empty list.
    if not os.path.exists(TASKS_FILE):
        return []
    
    with open(TASKS_FILE, "r") as f:
        content = f.read().strip()

    # If the file is empty, return an empty list.
    if not content:
        return []
    
    # json.loads() converts a JSON string into a Python object (in this case, a list of tasks).
    return json.loads(content)

# ─────────────────────────────────────────────
#  SAVE tasks back to the JSON file
# ─────────────────────────────────────────────

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        # json.dump() converts the Python list → JSON text and writes it to the file
        # indent=2 makes it human-readable (pretty printed with 2-space indentation)
        json.dump(tasks, f, indent=2)

# ─────────────────────────────────────────────
#  HELPER: generate the next available ID
# ─────────────────────────────────────────────

def next_id(tasks):
    # If there are no tasks yet, start at ID 1
    # Otherwise, find the highest existing ID and add 1
    # This means IDs never repeat, even after deleting tasks
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

# ─────────────────────────────────────────────
#  COMMAND: add a new task
#  Usage: task-cli add "description"
# ─────────────────────────────────────────────

def add_task(args):
    # args is everything the user typed after "add"
    # e.g. if user typed: task-cli add "Buy milk"
    # then args = ["Buy milk"]

    # Make sure the user actually gave us a description
    if not args:
        print("Error please provide the task description")
        print('Usage: task-cli add "your task here"')
        sys.exit(1)   # exit with code 1 = something went wrong

    description = args[0]
    tasks = load_tasks()
    new_task = {
        'id': next_id(tasks),
        'description': description,
        'status': 'todo',
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully with ID {new_task['id']}")


# ─────────────────────────────────────────────
#  COMMAND: update a task's description
#  Usage: task-cli update 1 "new description"
# ─────────────────────────────────────────────

def update_task(args):
    if len(args) < 2:
        print("Error: Please provide the task ID and the new description.")
        sys.exit(1)
    
    # BUG 4 FIXED: renamed 'id' to 'task_id' to avoid shadowing Python's built-in id()
    task_id = args[0]
    new_description = args[1]
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == int(task_id):
            task['description'] = new_description
            task['updated_at'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task with ID {task_id} updated successfully.")
            return
    print(f"Error: No task found with ID {task_id}.")
    sys.exit(1) 


# ─────────────────────────────────────────────
#  COMMAND: delete a task
#  Usage: task-cli delete 1
# ─────────────────────────────────────────────

def delete_task(args):
    if not args:
        print("Error: Please provide the task ID to delete.")
        sys.exit(1) 
    
    # BUG 4 FIXED: renamed 'id' to 'task_id' to avoid shadowing Python's built-in id()
    task_id = args[0]
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task['id'] == int(task_id):
            del tasks[i]
            save_tasks(tasks)
            print(f"Task with ID {task_id} deleted successfully.")
            return
    print(f"Error: No task found with ID {task_id}.")
    sys.exit(1)


# ─────────────────────────────────────────────
#  COMMAND: change a task's status
#  Called internally with status already set to "done" or "in-progress"
# ─────────────────────────────────────────────

def cmd_mark(args):
    if len(args) < 2:
        print("Error: Please provide the task ID and the new status.")
        sys.exit(1)
    
    # BUG 5 FIXED: validate that the status is one of the allowed values
    task_id = args[0]
    new_status = args[1]
    valid_statuses = {"todo", "in-progress", "done"}
    if new_status not in valid_statuses:
        print(f"Error: '{new_status}' is not a valid status.")
        print(f"Valid options: todo, in-progress, done")
        sys.exit(1)

    tasks = load_tasks()
    for task in tasks:
        if task['id'] == int(task_id):
            task['status'] = new_status
            task['updated_at'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task with ID {task_id} marked as '{new_status}' successfully.")
            return 
    print(f"Error: No task found with ID {task_id}.")
    sys.exit(1)


def mark_done(args):
    cmd_mark([args[0], "done"])


# ─────────────────────────────────────────────
#  COMMAND: list tasks (all or filtered by status)
#  Usage: task-cli list
#         task-cli list done
#         task-cli list todo
#         task-cli list in-progress
# ─────────────────────────────────────────────

def cmd_list(args=None):
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    
    # BUG 2 FIXED: filter tasks by status if the user provided one
    if args:
        status_filter = args[0]
        valid_statuses = {"todo", "in-progress", "done"}
        if status_filter not in valid_statuses:
            print(f"Error: '{status_filter}' is not a valid status.")
            print("Valid options: todo, in-progress, done")
            sys.exit(1)
        tasks = [task for task in tasks if task['status'] == status_filter]
        if not tasks:
            print(f"No tasks with status '{status_filter}'.")
            return

    for task in tasks:
        print(f"ID: {task['id']}")
        print(f"Description: {task['description']}")
        print(f"Status: {task['status']}")
        print(f"Created At: {task['created_at']}")
        print(f"Updated At: {task['updated_at']}")
        print("-" * 20) 


# ─────────────────────────────────────────────
#  HELP message
# ─────────────────────────────────────────────

def print_help():
    print("Task Tracker CLI")
    print("Usage: python3 tasks.py [command] [arguments]")
    print("Commands:")
    print('  add "description"            - Add a new task with the given description')
    print('  update ID "new description"  - Update the description of the task with the given ID')
    print("  delete ID                    - Delete the task with the given ID")
    print("  mark-in-progress ID          - Mark the task with the given ID as in-progress")
    print("  mark-done ID                 - Mark the task with the given ID as done")
    print("  list                         - List all tasks")
    print("  list todo                    - List only todo tasks")
    print("  list in-progress             - List only in-progress tasks")
    print("  list done                    - List only done tasks")
    print("  help                         - Show this help message")


# ─────────────────────────────────────────────
#  MAIN — the entry point of the program
# ─────────────────────────────────────────────

def main():
    # sys.argv is a list of everything the user typed
    # sys.argv[0] = the script name itself ("task-cli.py")
    # sys.argv[1] = the command ("add", "list", etc.)
    # sys.argv[2:] = everything after the command (the arguments)

    # If the user typed nothing after the script name, show help
    if len(sys.argv) < 2:
        print_help()
        sys.exit(0)

    command = sys.argv[1].lower()
    args = sys.argv[2:]

    if command == 'add':
        add_task(args)

    elif command == 'update':
        update_task(args)

    elif command == 'delete':
        delete_task(args)

    elif command == 'mark-in-progress':
        # BUG 3 FIXED: guard against missing ID before accessing args[0]
        if not args:
            print("Error: please provide a task ID.")
            sys.exit(1)
        cmd_mark([args[0], "in-progress"])

    elif command == 'mark-done':
        # BUG 1 FIXED: was 'mark_done' (underscore) — user types hyphen so it never matched
        # BUG 3 FIXED: guard against missing ID before accessing args[0]
        if not args:
            print("Error: please provide a task ID.")
            sys.exit(1)
        cmd_mark([args[0], "done"])

    elif command == "list":
        cmd_list(args)

    elif command == 'help':
        print_help()
    
    else:
        print(f"Unknown Command: '{command}'.")
        print("Run 'python3 tasks.py help' to see all commands")
        sys.exit(1)

    
if __name__ == "__main__":
    main()