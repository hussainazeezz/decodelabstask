# ==========================================
# Task 1: To-Do List
# Name: Muhammad Hussain
# Email: hussainazeezz@outlook.com
# ==========================================

def display_menu():
    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    print("================================")


tasks = []

while True:
    display_menu()

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 4.")
        continue

    if choice == 1:
        task = input("Enter your task: ").strip()

        if task:
            tasks.append(task)
            print("Task added successfully!")
        else:
            print("Task cannot be empty.")

    elif choice == 2:
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

    elif choice == 3:
        if not tasks:
            print("No tasks available to delete.")
        else:
            print("\nYour Tasks:")
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

            try:
                task_number = int(input("Enter task number to delete: "))
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
                continue

            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                print(f'"{deleted_task}" deleted successfully!')
            else:
                print("Invalid task number.")

    elif choice == 4:
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please select between 1 and 4.")
