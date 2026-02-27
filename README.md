# 🐍 Python Projects Collection

<div align="center">

A comprehensive collection of **three beginner-friendly Python CLI applications** demonstrating core programming concepts.

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Educational-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success)](README.md)

</div>

---

## 📚 Projects Overview

Each project demonstrates core Python concepts including **file I/O**, **data structures**, **user input handling**, and **JSON persistence**.

<br/>

### 1️⃣ 🔐 Password Generator

| | |
|---|---|
| **Description** | Secure password generation & user credential management with persistent storage |
| **Difficulty** | ⭐ Beginner → File I/O & Database Basics |
| **Key Focus** | Data persistence, input validation, file operations |

#### ✨ Key Features
```
✓ Generate 10-character secure alphanumeric passwords
✓ Add users with automatic duplicate prevention
✓ View all registered users in database
✓ Search users by phone number
✓ Delete users from database
✓ Persistent JSON storage
```

#### 🚀 Quick Start
```bash
cd Password_Generator
python3 main.py
```

#### 📦 Technologies & Modules
| Technology | Purpose |
|------------|---------|
| Python 3.x | Core language |
| JSON | Data storage |
| `secrets` module | Secure password generation |
| `string` module | Character sets |

#### 📂 Project Structure
```
Password_Generator/
├── main.py      # Main application with user management functions
├── db.py        # Database module (load/save JSON)
├── users.json   # User data storage (auto-generated)
└── Readme.md    # Project documentation
```

<br/>

---

### 2️⃣ 🎮 Number Guessing Game

| | |
|---|---|
| **Description** | Interactive number guessing game with real-time feedback |
| **Difficulty** | ⭐ Beginner → Core Language Fundamentals |
| **Key Focus** | Loops, conditionals, random number generation |

#### ✨ Key Features
```
✓ Set custom lower and upper bounds
✓ 7 attempts to guess the correct number
✓ Real-time feedback (too high/too low)
✓ Attempt counter
✓ Replay as many times as desired
✓ Simple & intuitive UI
```

#### 🚀 Quick Start
```bash
cd "Number Guessing Game"
python3 numbGuess.py
```

#### 📦 Technologies & Modules
| Technology | Purpose |
|------------|---------|
| Python 3.x | Core language |
| `random` module | Generate random numbers |

#### 📂 Project Structure
```
Number Guessing Game/
├── numbGuess.py  # Game logic & prompts
└── Readme.md     # Project documentation
```

#### 🎯 Example Gameplay
```
Enter the Lower Bound: 1
Enter the Higher Bound: 100
Enter your guessed number: 50
→ Too High, Try a lower number

Enter your guessed number: 25
→ Too Low, Try a higher number

Enter your guessed number: 40
→ Correct! The number is 40. You guessed it in 3 attempts
```

<br/>

---

### 3️⃣ ✅ Task Tracker CLI

| | |
|---|---|
| **Description** | Lightweight command-line task manager with JSON persistence |
| **Difficulty** | ⭐⭐⭐ Intermediate-Advanced → CLI Development |
| **Key Focus** | CLI design, state management, timestamps |

#### ✨ Key Features
```
✓ Add tasks with descriptions
✓ Update task descriptions
✓ Delete tasks from list
✓ Mark tasks as in-progress or done
✓ List all tasks or filter by status
✓ Automatic task ID generation
✓ Timestamps for creation & updates
✓ Persistent JSON storage
```

#### 🚀 Quick Start
```bash
cd Task-Tracker-CLI

# Add a task
python3 tasks.py add "Buy groceries"

# View all tasks
python3 tasks.py list

# Update a task
python3 tasks.py update 1 "Buy oat milk"

# Delete a task
python3 tasks.py delete 1
```

#### 📦 Technologies & Modules
| Technology | Purpose |
|------------|---------|
| Python 3.14.3+ | Core language |
| JSON | Data storage |
| `sys` module | CLI argument parsing |
| `datetime` module | Timestamps |

#### 📂 Project Structure
```
Task-Tracker-CLI/
├── tasks.py      # CLI entry point & task logic
├── tasks.json    # Task data storage (auto-generated)
└── Readme.md     # Project documentation
```

---

## 🚀 Getting Started

### ✅ Prerequisites

| Requirement | Details |
|---|---|
| **Python Version** | Python 3.14.3 or higher installed on your system |
| **Check Version** | `python3 --version` |
| **Terminal** | Terminal (macOS/Linux) or PowerShell/CMD (Windows) |

### 📥 Installation

1. **Clone or download** this repository
2. **Navigate** to the Python directory:
   ```bash
   cd /path/to/Python
   ```
3. **Navigate** to any project folder and run its main file

### ▶️ Running Each Project

| Project | Command |
|---------|---------|
| **Password Generator** | `cd Password_Generator && python3 main.py` |
| **Number Guessing Game** | `cd "Number Guessing Game" && python3 numbGuess.py` |
| **Task Tracker CLI** | `cd Task-Tracker-CLI && python3 tasks.py [command] [args]` |

---

## 📖 Detailed Usage Guide

<br/>

### 🔐 Password Generator

#### Main Menu Options
```
═══════════════════════════════════════
    Password Manager
═══════════════════════════════════════
1. Add User          → Create new user with auto-generated password
2. View All Users    → Display all registered users
3. Search User       → Find user by phone number
4. Delete User       → Remove user from database
5. Exit              → Close the application
═══════════════════════════════════════
```

#### Features in Detail
| Feature | Description |
|---------|---|
| **Add User** | Enter name and phone number, receive generated password |
| **View All Users** | See all users with their details |
| **Search User** | Look up user by their phone number |
| **Delete User** | Remove user completely from database |
| **Data Persistence** | All data is saved to `users.json` |

<br/>

### 🎮 Number Guessing Game

#### How to Play
```
1️⃣  Set the lower bound (e.g., 1)
2️⃣  Set the upper bound (e.g., 100)
3️⃣  Guess the number within 7 attempts
4️⃣  Receive feedback on each guess
5️⃣  Win by guessing correctly or lose if attempts run out
```

<br/>

### ✅ Task Tracker CLI

#### Available Commands
```bash
# ─────────────────────────────────────
# Add a task
python3 tasks.py add "Task description"

# ─────────────────────────────────────
# List all tasks
python3 tasks.py list

# ─────────────────────────────────────
# Mark task as in-progress
python3 tasks.py mark-in-progress 1

# ─────────────────────────────────────
# Mark task as done
python3 tasks.py mark-done 1

# ─────────────────────────────────────
# Update task description
python3 tasks.py update 1 "New description"

# ─────────────────────────────────────
# Delete a task
python3 tasks.py delete 1
# ─────────────────────────────────────
```

---

## 💾 Data Storage

All projects that require data persistence use **JSON file storage** for easy data management and portability.

<br/>

### 📋 Password Generator - `users.json`

```json
[
  {
    "name": "John Doe",
    "phone": "9876543210",
    "password": "aB3cD9eF1x"
  },
  {
    "name": "Jane Smith",
    "phone": "9123456789",
    "password": "xY7zW2qR4p"
  }
]
```

**Structure:**
| Field | Type | Description |
|-------|------|---|
| `name` | String | User's full name |
| `phone` | String | User's phone number (unique identifier) |
| `password` | String | Auto-generated secure password |

<br/>

### 📋 Task Tracker - `tasks.json`

```json
[
  {
    "id": 1,
    "description": "Buy groceries",
    "status": "done",
    "createdAt": "2025-02-27T10:30:00",
    "updatedAt": "2025-02-27T14:45:00"
  },
  {
    "id": 2,
    "description": "Complete project",
    "status": "in-progress",
    "createdAt": "2025-02-27T11:00:00",
    "updatedAt": "2025-02-27T15:20:00"
  }
]
```

**Structure:**
| Field | Type | Description |
|-------|------|---|
| `id` | Integer | Unique task identifier |
| `description` | String | Task description/title |
| `status` | String | Task status: `todo`, `in-progress`, or `done` |
| `createdAt` | String | ISO timestamp of creation |
| `updatedAt` | String | ISO timestamp of last update |

---

## 🔧 Error Handling & Robustness

All projects include robust error handling mechanisms:

| Feature | Description |
|---------|---|
| **Input Validation** | Ensures non-empty inputs and correct data types |
| **File Operations** | Graceful handling of missing or corrupted files |
| **Duplicate Prevention** | Prevents duplicate user registrations (Password Generator) |
| **Keyboard Interrupt** | Clean exit on Ctrl+C |
| **Exception Management** | Comprehensive try-catch blocks for stability |

<br/>

---

## 📝 Learning Outcomes

These projects teach fundamental programming concepts:

| Concept | Projects | Details |
|---------|----------|---------|
| **Loops & Conditionals** | All projects | Control flow and decision making |
| **Functions** | All projects | Code reusability and organization |
| **File I/O** | Password Generator, Task Tracker | Reading and writing to files |
| **JSON Handling** | Password Generator, Task Tracker | Data serialization and storage |
| **User Input Validation** | All projects | Data integrity and error prevention |
| **Random Number Generation** | Number Guessing Game | Probability and randomization |
| **CLI Development** | Task Tracker | Command-line argument parsing |
| **Timestamps** | Task Tracker | Date and time handling |
| **Data Structures** | All projects | Lists and dictionaries |
| **Error Handling** | All projects | Exception management and recovery |

---

## 🤝 Contributing

<div align="center">

Feel free to enhance these projects!

</div>

| Type | Description |
|------|---|
| 🎨 **Features** | Add new features to any project |
| 🐛 **Bug Fixes** | Improve error handling and robustness |
| ✨ **UX** | Enhance user experience and interface |
| 🧪 **Testing** | Add unit tests and integration tests |
| ⚡ **Performance** | Optimize code performance |
| 📚 **Documentation** | Improve README and code comments |

---

## 📄 License

These projects are **free to use and modify** for educational purposes.

---

## 📬 Support & Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| **Python not found** | Install Python 3.x from [python.org](https://www.python.org/) |
| **Module not found** | Ensure you're running from the project directory |
| **JSON file corrupted** | Delete the JSON file and restart the application |
| **Encoding errors** | Try running with UTF-8 encoding: `PYTHONIOENCODING=utf-8` |

### Getting Help

1. ✅ Check individual project README files
2. ✅ Verify Python version compatibility
3. ✅ Ensure JSON files are not corrupted
4. ✅ Try running from the project directory
5. ✅ Review error messages carefully

---

## 🎯 Project Difficulty & Roadmap

| Project | Difficulty | Learning Path | Best For |
|---------|-----------|---|----------|
| 🎮 Number Guessing Game | ⭐ Beginner | Start here → Fundamentals | Learning Python basics |
| 🔐 Password Generator | ⭐⭐ Intermediate | Next → File I/O | File operations & databases |
| ✅ Task Tracker CLI | ⭐⭐⭐ Advanced | Final → Full stack | CLI development |

---

## 📊 Project Statistics

| Metric | Value |
|--------|-------|
| **Total Projects** | 3 |
| **Total Files** | ~10 |
| **Languages** | Python 3.x |
| **Storage Format** | JSON |
| **Lines of Code** | ~350+ |
| **Difficulty Range** | Beginner → Advanced |

<br/>

---

<div align="center">

### 🌟 Ready to Get Started?

Choose a project above and begin your Python journey!

**Happy Coding! 🚀**

</div>







