tasks = []


def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass


def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def add_task():
    task = input("Enter a task: ").strip()

    if task:
        tasks.append(task)
        save_tasks()
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour To-Do List:")

        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")


def remove_task():
    view_tasks()

    if tasks:
        try:
            number = int(input("Enter task number to remove: "))

            if 1 <= number <= len(tasks):
                removed_task = tasks.pop(number - 1)
                save_tasks()
                print(f"Removed: {removed_task}")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")


def main():
    load_tasks()

    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            remove_task()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()