# This is a simple console-based Todo List Manager.
# How to use:
# - Run the script and follow the menu prompts to add, view, or remove tasks.
# - Tasks are stored in memory during runtime only.

def display_menu():
    print("\nTodo List Manager")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Remove a task")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter the new task: ")
    tasks.append(task)
    print(f"Task added: {task}")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task(tasks):
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting Todo List Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()