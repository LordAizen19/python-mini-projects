# Python CLI Projects Collection

A collection of command-line applications built as part of the [roadmap.sh](https://roadmap.sh) backend development track. These projects demonstrate practical Python programming skills, CLI design patterns, and progressive problem-solving through hands-on development.

**Repository:** https://github.com/LordAizen19/python-projects

## Tech Stack

- **Language:** Python 3.x
- **Core Libraries:** 
  - `random` - Random number generation
  - `sys` - Command-line argument parsing
  - `os` - File system operations
  - `json` - Data persistence
  - `datetime` - Timestamp management
- **Approach:** Pure Python with standard library only (no external dependencies)

## Projects

### 1. Number Guessing Game
A classic guessing game where players attempt to identify a randomly generated number within a user-defined range.

### 2. Task Tracker CLI
A command-line task management system with JSON-based persistence and status tracking capabilities (in development).

---

## Features

### Number Guessing Game
- User-defined number range (lower and upper bounds)
- 7-attempt limit with attempt counter
- Real-time feedback system (too high/too low hints)
- Win/lose condition handling
- Input validation for numeric entries

### Task Tracker CLI (Current Implementation)
- Modular CLI architecture with command routing
- JSON file-based persistence design
- Unique ID generation system for tasks
- Command-line argument parsing via `sys.argv`
- Extensible command structure (add, update, delete, mark, list)
- Error handling with user-friendly messages

---

## Installation

### Prerequisites
- Python 3.6 or higher
- Terminal/Command Prompt

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/LordAizen19/python-projects.git
   cd python-cli-projects
   ```

2. **Verify Python installation**
   ```bash
   python3 --version
   ```

3. **No additional dependencies required** – all projects use Python's standard library.

---

## Usage

### Number Guessing Game

```bash
cd "Number Guessing Game"
python3 numbGuess.py
```

**Example Session:**
```
Hi! Welcome to the Number Guessing Game.
You have 7 chances to guess the number. Let's start!
Enter the Lower Bound: 1
Enter the Higher Bound: 100
Enter your guessed number: 50
Too High, Try a lower number
Enter your guessed number: 25
Too Low, Try a higher number
Enter your guessed number: 37
Correct!, The number is 37. You guessed it in 3 attempts
Game Ends
```

### Task Tracker CLI

```bash
cd Task-Tracker-CLI
python3 tasks.py <command> [arguments]
```

**Planned Commands:**
```bash
# Add a new task
python3 tasks.py add "Buy groceries"

# Update a task
python3 tasks.py update <task_id> "Updated description"

# Delete a task
python3 tasks.py delete <task_id>

# Mark task in progress
python3 tasks.py mark-in-progress <task_id>

# Mark task as done
python3 tasks.py mark-done <task_id>

# List all tasks
python3 tasks.py list

# Show help
python3 tasks.py help
```

---

## Project Structure

```
.
├── README.md
├── Number Guessing Game/
│   └── numbGuess.py          # Main game logic with randomization
└── Task-Tracker-CLI/
    ├── tasks.py              # CLI interface and command handlers
    └── tasks.json            # JSON data store (auto-generated)
```

### Key Files

- **numbGuess.py**: Implements game loop, random number generation, attempt tracking, and user feedback logic.
- **tasks.py**: Contains CLI argument parsing, JSON I/O operations, command routing system, and helper functions for task management.

---

## What I Learned

### Core Programming Concepts
- **Control Flow**: Implementing game loops with `while`, conditional branching with `if/elif/else`
- **Random Module**: Using `random.randint()` for unpredictable number generation
- **User Input Handling**: Type casting and validation of user entries
- **Functions**: Breaking code into reusable, single-purpose functions

### CLI Development Patterns
- **Argument Parsing**: Using `sys.argv` to capture and route commands
- **Command Design**: Building a scalable command structure (verb-noun pattern)
- **Exit Codes**: Proper use of `sys.exit()` with status codes (0 for success, 1 for errors)
- **User Experience**: Providing clear error messages and usage instructions

### Data Persistence
- **JSON Operations**: Converting Python objects to JSON with `json.dump()` and parsing with `json.loads()`
- **File I/O**: Reading and writing files safely with context managers (`with` statements)
- **Edge Case Handling**: Managing empty files, missing files, and malformed data

### Software Architecture
- **Separation of Concerns**: Dividing code into distinct helper functions (load, save, business logic)
- **Constants**: Using uppercase naming for configuration values (e.g., `TASKS_FILE`)
- **ID Management**: Implementing auto-incrementing IDs to prevent conflicts after deletions

---

## Challenges & Solutions

### Challenge 1: Handling Empty/Missing JSON Files
**Problem:** Application crashed when `tasks.json` didn't exist or was empty.

**Solution:** 
- Implemented `os.path.exists()` check before file operations
- Added `.strip()` validation to detect empty files
- Return empty list as default fallback

```python
if not os.path.exists(TASKS_FILE):
    return []
if not content:
    return []
```

### Challenge 2: Designing a Scalable CLI Interface
**Problem:** Needed a way to handle multiple commands without if-else bloat.

**Solution:**
- Created a command router in `main()` using dictionary-like dispatching approach
- Separated each command into its own function for maintainability
- Standardized argument passing pattern (`args` list)

### Challenge 3: User-Friendly Error Messages
**Problem:** Cryptic Python errors confused users unfamiliar with programming.

**Solution:**
- Wrapped operations in validation checks before execution
- Provided custom error messages with usage examples
- Used `sys.exit(1)` to terminate gracefully on invalid input

---

## Future Improvements

### Task Tracker CLI
- [ ] Complete implementation of update, delete, and mark functions
- [ ] Add task filtering by status (todo, in-progress, done)
- [ ] Implement due date tracking with `datetime` comparisons
- [ ] Add task priority levels (low, medium, high)
- [ ] Create a formatted table output using string padding
- [ ] Add search functionality (find tasks by keyword)
- [ ] Implement undo/redo feature with command history

### Number Guessing Game
- [ ] Add difficulty levels (easy: 10 tries, hard: 5 tries)
- [ ] Implement scoring system based on attempts used
- [ ] Track high scores in a JSON leaderboard
- [ ] Add multiplayer mode (players take turns)

### General
- [ ] Add unit tests using `unittest` or `pytest`
- [ ] Create shell scripts for easier execution
- [ ] Add color output using `colorama` library
- [ ] Implement logging for debugging

---

## Demo

### Number Guessing Game
```
Current Status: ✅ Fully Functional
```
### Task Tracker CLI
```
Current Status: 🚧 Architecture Complete, Commands In Progress
```
---

## Contributing

Contributions, issues, and feature requests are welcome! This is a learning project, so feel free to:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Guidelines
- Follow existing code style and structure
- Add comments for complex logic
- Test your changes before submitting
- Update README if adding new features

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Acknowledgments

- Project ideas from [roadmap.sh](https://roadmap.sh/projects)
- Built as part of backend development learning path
- Focused on practical CLI development and Python fundamentals