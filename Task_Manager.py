print("--- My Task Manager ---")

tasks = []

# infinite loop
while True:
    # get user input for command
    command = input("Enter a command (add / view / remove / exit) : ")

    if command == 'add':
        task = input("Enter your task you want to do : ")
        tasks.append(task)
        print("Your Task has been added!")

    elif command == 'exit':
        break

    elif command == 'view':
        print("--- Your Tasks ---")
        # index is the number [1,2, 3 ....], task is the text
        for index, task in enumerate(tasks, 1):
            print(f"{index}, {task}")
        print("-----------")

    elif command == 'remove':

        if not tasks:
            print("List is empty , nothing to remove")
            continue

        # ask for the number to remove
        try:
            number = int(input("Enter the point number which you want to remove : "))

            if 0 < number <= len(tasks) :
                removed_item = tasks.pop(number - 1)
                print(f" Removed : {removed_item}")
            else :
                print(f'Enter the valid number between 1 and {len(tasks)}')

        except ValueError:
            print("Error : PLease enter the valid number.")

