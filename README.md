# Python-Mini-Projects


This repository documents my journey from zero to backend engineering. It focuses on **Active Recall** and **Micro-Projects** rather than passive tutorial watching.

## 📂 Project 1: The CLI Task Manager (Basic)
**Goal:** Build a functional command-line tool using core Python syntax without relying on external libraries.

### 🚀 Features
* **Infinite Loop:** The program runs continuously until the user chooses to exit.
* **Persistent List:** Stores tasks in memory using a Python List.
* **Dynamic Removal:** Users can delete tasks by their number (Index).
* **Input Validation:** Prevents crashes using basic conditional logic.

### 🧠 Concepts Mastered
* `while True` loops for continuous execution.
* **Lists (`[]`)**: Appending and popping items.
* **Conditionals**: `if/elif/else` for command routing.
* **Enumerate**: `enumerate(list, 1)` to display user-friendly numbered lists.

---

## 📂 Project 2: Task Manager Pro (Structured Data)
**Goal:** Upgrade the basic tool to handle complex data structures, state management, and robust error handling.

### 🚀 Upgrades from V1
* **Data Structure Shift:** Moved from a simple `List of Strings` to a `List of Dictionaries`. This allows tracking multiple properties (Title + Status) for a single task.
* **State Management:** Implemented an **Edit** feature to mutate specific tasks in memory.
* **Formatting:** Used **f-string padding** (e.g., `{:<8}`) to create a clean, table-like UI in the terminal.
* **Crash Protection:** Implemented `try/except` blocks to handle `ValueError` (e.g., if a user types "apple" instead of a number).

### 🧠 Concepts Mastered
* **Dictionaries (`{}`)**: Key-Value pairs for structured data simulation.
* **Tuples (`()`)**: Used for immutable constants (`VALID_STATUSES`).
* **Reference vs Copy**: Understanding how modifying a variable updates the original list.
* **Exception Handling**: Using `try/except` to prevent `IndexError` and `ValueError`.

---

## 🛠️ How to Run
1.  Clone the repository:
    ```bash
    git clone [https://github.com/LordAizen19/python-mastery-roadmap.git]
    ```
2.  Navigate to the project directory:
    ```bash
    cd python-mastery-roadmap
    ```
3.  Run the script:
    ```bash
    python Task_Manager.py
    ```

## 📈 Roadmap
- [x] Day 1-5: Syntax Basics (Lists, Loops)
- [x] Day 6: Build CLI Tool (CRUD Operations)
- [ ] Day 7-14: OOP & APIs
- [ ] Day 15+: Django & Database Integration