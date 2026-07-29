# TO-DO LIST APP

todo_list = []


def show_tasks():
    if len(todo_list) == 0:
        print("\nNo tasks in the list.\n")
    else:
        print("\nYour Tasks:")
        for i in range(len(todo_list)):
            print(f"{i + 1}. {todo_list[i]}")
        print()


def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print("Task added successfully!\n")


def remove_task():
    if len(todo_list) == 0:
        print("No tasks to remove.\n")
        return

    show_tasks()

    try:
        task_number = int(input("Enter task number to remove: "))

        if 1 <= task_number <= len(todo_list):
            removed = todo_list.pop(task_number - 1)
            print(f"'{removed}' removed successfully!\n")
        else:
            print("Invalid task number.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def main():
    while True:
        print("===== TO-DO LIST =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()

        elif choice == "2":
            add_task()

        elif choice == "3":
            remove_task()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.\n")


main()