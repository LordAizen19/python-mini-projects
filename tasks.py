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
# HELPER FUNCTIONS\
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
        json.dump(tasks, f, indent = 2)

# ─────────────────────────────────────────────
#  HELPER: generate the next available ID
# ─────────────────────────────────────────────

def next_id(tasks):
    # If there are no tasks yet, start at ID 1
    # Otherwise, find the highest existing ID and add 1
    # This means IDs never repeat, even after deleting tasks
    if not tasks:
        return 1
    return max(tasks[id] for task in tasks) + 1

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

def update_task(args):
    pass

def delete_task(args):
    pass

def cmd_mark(args):
    pass

def mark_done(args):
    pass

def cmd_list(args):
    pass

def print_help():
    pass
    
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
        cmd_mark(args, "in-progress")

    elif command == 'mark_done':
        mark_done(args, "done")

    elif command == "list":
        cmd_list()

    elif command == 'help':
        print_help()
    
    else:
        print(f"Unknown Command: '{command}'.")
        print("Run 'python3 tasks.py help' to see all commands")
        sys.exit(1)

    
if __name__ == "__main__":
    main()
