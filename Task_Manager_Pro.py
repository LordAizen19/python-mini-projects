# using tuple because these actions should not change
VALID_STATUES = ("Pending" , "Done")

# list is main container of our data
tasks = []

print("--- Pro Task Manager ---")
print("Commands : ( add, view, remove, edit, exit)")

while True:
    command = input("\n> Enter a command : ").lower().strip()  # lower makes the command case-insensitive

    # Add Command
    if command == 'add':
        title = input("Enter the task title : ")

        # Dictionary : Grouping related data together
        new_task = {
            "title" : title,
            "status" : "Pending"
        }
        tasks.append(new_task)
        print(f"Saved : {title}")

    # view command
    elif command == 'view':
        print("\nID  | Status  | Title")
        print("-" * 30)

        # enumerate gives us the index i and the dictionary [task]
        for i , task in enumerate(tasks, 1):
            #  We access values using Keys: task['status']
            print(f"{i:<3} | {task['status']:<8} | {task['title']}")
        print("-" * 30)

    # edit command
    elif command == 'edit':
        try:
            idx = int(input("Enter id to edit : ")) - 1

            if 0 < idx < len(tasks):
                selected_task = tasks[idx]
                print(f"Current Status : {selected_task['status']}")
                new_status = input(f"New Status : {VALID_STATUES}: ")

                if new_status in VALID_STATUES:
                    selected_task['status'] = new_status
                    print("Status updated successfully")
                else:
                    print("Invalid Status Type")
            else:
                print("Id not found")
        except ValueError:
            print("Error: Please enter a number. ")

    # remove command
    elif command == 'remove':
        try:
            idx = int(input("Enter the id to remove : ")) - 1

            if 0 < idx < len(tasks):
                removed_task = tasks.pop(idx)
                print(f"Removed task : {removed_task['title']}")
            else:
                print("Error : Out of Range")
        except ValueError:
            print("Error: Enter the valid ID")

    # exit command
    elif command == 'exit':
        print("Saving ... (nor really , just imagine!) Bye.")
        break
    else:
        print("Unknown Command")
