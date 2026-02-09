print("-------------------------Welcome Harsh!, Let's build our Todo List CLI ------------------------")

def show_menu():
    pass

def add_task():
    pass

def view_task():
    pass

def edit_task():
    pass

def delete_task():
    pass


def main():
    tasks = []
    commands = ["add", "view", "edit", "delete", "exit"]
    while True:
        show_menu(commands)
        option = input("Choose an option: ")

        if option == "0":
            add_task(tasks)
        elif option == "1":
            view_task(tasks)
        elif option == "2":
            edit_task(tasks)
        elif option == "3":
            delete_task(tasks)
        elif option == "4":
            print("GoodBye! :)")
            break


if __name__ == "__main__":
    main()