import secrets
import string
from db import load_data, save_data


def generate_password():
    """Generate a random 10-character alphanumeric password."""
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(10))


def prompt_non_empty(prompt, *, digits_only=False):
    """Prompt until a non-empty value is provided; optionally enforce digits-only."""
    while True:
        value = input(prompt).strip()
        if not value:
            print("Input cannot be empty. Please try again.")
            continue
        if digits_only and not value.isdigit():
            print("Phone number must contain digits only.")
            continue
        return value


def add_user():
    """Prompt for user details and save a new user if not already present."""
    name = prompt_non_empty("Enter your name: ")
    phone = prompt_non_empty("Enter your phone number: ", digits_only=True)

    try:
        data = load_data()
    except (OSError, ValueError) as exc:
        print(f"Failed to load users: {exc}")
        return

    for user in data:
        if user["phone"] == phone and user["name"] == name:
            print("User with this phone number already exits")
            return

    password = generate_password()

    user = {
        "name": name,
        "phone": phone,
        "password": password
    }

    data.append(user)
    try:
        save_data(data)
    except OSError as exc:
        print(f"Failed to save user: {exc}")
        return
    print(f"Successfully saved, {password}")
    print(user)


def view_all_users():
    """Print all saved users, or a message if none exist."""
    try:
        data = load_data()
    except (OSError, ValueError) as exc:
        print(f"Failed to load users: {exc}")
        return
    if not data:
        print("No users found!")
        return

    for i, user in enumerate(data, start=1):
        print(f"{i}, Name: {user['name']} |Phone: {user['phone']} |Password: {user['password']}")


def search_user():
    """Search for a user by phone number and print details if found."""
    try:
        data = load_data()
    except (OSError, ValueError) as exc:
        print(f"Failed to load users: {exc}")
        return
    if not data:
        print("No entries found!")
        return

    phone = prompt_non_empty("Enter the phone of the user to search: ", digits_only=True)

    for user in data:
        if user["phone"] == phone:
            print(f"User found! Name: {user['name']} |Password: {user['password']}")
            return

    print("User not found! Check the phone number and try again.")


def delete_user():
    """Delete a user by phone number if present."""
    try:
        data = load_data()
    except (OSError, ValueError) as exc:
        print(f"Failed to load users: {exc}")
        return
    if not data:
        print("No entries found!")
        return

    phone = prompt_non_empty("Enter the phone of the user to delete: ", digits_only=True)

    for user in data:
        if user["phone"] == phone:
            data.remove(user)
            try:
                save_data(data)
            except OSError as exc:
                print(f"Failed to save users: {exc}")
                return
            print("User Deleted!")
            return

    print("User not found! Check the phone number and try again.")


if __name__ == "__main__":
    while True:
        try:
            print("\n--- Password Manager ---")
            print("1. Add User")
            print("2. View All Users")
            print("3. Search User")
            print("4. Delete User")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                add_user()
            elif choice == "2":
                view_all_users()
            elif choice == "3":
                search_user()
            elif choice == "4":
                delete_user()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as exc:
            print(f"Unexpected error: {exc}")
