# Task Tracker CLI

A lightweight command-line task manager that stores tasks in a JSON file and supports common task workflows.

## 📋 Project Overview

This CLI lets you:
- Add tasks with descriptions
- Update task descriptions
- Delete tasks
- Mark tasks as in-progress or done
- List all tasks or filter by status

## 📁 Project Structure

```
Task-Tracker-CLI/
├── tasks.py         # CLI entry point and task logic
├── tasks.json       # Task data storage (auto-generated)
└── Readme.md        # Project documentation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.14.3 or higher installed on your system

### Usage

Run any command like this:
```bash
python3 tasks.py [command] [arguments]
```

### Commands

- Add a task:
```bash
python3 tasks.py add "Buy milk"
```

- Update a task:
```bash
python3 tasks.py update 1 "Buy oat milk"
```

- Delete a task:
```bash
python3 tasks.py delete 1
```

- Mark in progress:
```bash
python3 tasks.py mark-in-progress 1
```

- Mark done:
```bash
python3 tasks.py mark-done 1
```

- List tasks:
```bash
python3 tasks.py list
python3 tasks.py list todo
python3 tasks.py list in-progress
python3 tasks.py list done
```

- Help:
```bash
python3 tasks.py help
```

## 💾 Data Storage

Tasks are stored in `tasks.json` with fields like:
- `id`
- `description`
- `status` (todo, in-progress, done)
- `created_at`
- `updated_at`

The file is created automatically the first time you add a task.
