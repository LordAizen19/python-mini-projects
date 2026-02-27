# Password Generator

A simple command-line application for generating secure random passwords and managing user credentials with persistent storage.

## 📋 Project Overview

This project provides a Password Generator tool that allows you to:
- Generate secure random passwords for users
- Store user information (name, phone number, and generated password)
- Prevent duplicate registrations
- Search and delete users
- Persist user data to a JSON file for later retrieval

## 📁 Project Structure

```
Password_Generator/
├── main.py          # Main application entry point with user management functions
├── db.py            # Database module for loading and saving user data
├── users.json       # JSON file storing user credentials (auto-generated)
└── Readme.md        # Project documentation
```

## 📚 File Descriptions

### `main.py`
The main application file containing core functionality:
- **`generate_password()`**: Generates a 10-character random password using letters and digits
- **`prompt_non_empty()`**: Ensures name/phone inputs are not empty (and phone is digits-only)
- **`add_user()`**: Adds a user with duplicate checks and auto-generated password
- **`view_all_users()`**: Lists all saved users
- **`search_user()`**: Searches for a user by phone number
- **`delete_user()`**: Deletes a user by phone number

### `db.py`
Database management module with two key functions:
- **`load_data()`**: Loads user data from `users.json`. Returns an empty list if the file doesn't exist yet
- **`save_data(data)`**: Saves user data to `users.json` with formatted indentation for readability

### `users.json`
JSON file that stores all registered users in the following format:
```json
[
  {
    "name": "User Name",
    "phone": "Phone Number",
    "password": "Generated Password"
  }
]
```

## 🚀 Getting Started

### Prerequisites
- Python 3.14.3 or higher installed on your system

### Installation
No external dependencies are required. This project uses only Python's built-in libraries:
- `secrets` - For secure random password generation
- `string` - For character sets
- `json` - For data persistence
- `os` - For file existence checking

### Usage

Run the application:
```bash
python3 main.py
```

Follow the on-screen menu to add, view, search, and delete users.

## ✨ Features

- **Secure Password Generation**: Uses Python's `secrets` module for cryptographically secure random passwords
- **Input Validation**: Rejects empty input and non-digit phone numbers
- **Data Persistence**: Automatically saves user data to `users.json`
- **Duplicate Prevention**: Prevents registering multiple users with the same name and phone
- **User-Friendly Menu**: Clear prompts for common actions

## 📊 Example Output

When a user is added successfully:
```
Successfully saved, kkjqCBMumz
{'name': 'John Doe', 'phone': '1234567890', 'password': 'kkjqCBMumz'}
```

## 🔒 Security Notes

- Passwords are generated using Python's `secrets` module for cryptographic randomness
- The `users.json` file stores passwords in plain text. For production use, consider implementing password hashing (e.g., using `bcrypt`)

## 📝 Error Handling

- Duplicate entries show: "User with this phone number already exits"
- Empty input and non-digit phone numbers are rejected with clear prompts
- The application gracefully creates `users.json` on first run

## 🔄 Related Projects

- [Number Guessing Game](../Number%20Guessing%20Game/Readme.md)
- [Task Tracker CLI](../Task-Tracker-CLI/Readme.md)

## 🔄 Future Enhancements

- Add password hashing for better security
- Add update/edit user features
- Support exporting user data
