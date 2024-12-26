import main
import json

# List of tasks for managing the To-Do List
tasks = []

def display_menu():
    """
    Display the main menu for selecting options.
    """
    print("\n --- WELCOME TO TO-DO LIST ---")
    print("1. Add a task.")
    print("2. Show tasks.")
    print("3. Remove a task.")
    print("4. Save tasks to file.")
    print("5. Load tasks from file.")
    print("6. EXIT!")

def add_task():
    """
    Add a new task to the task list.
    """
    task_name = input("Enter the task name: ")
    tasks.append(task_name)
    print(f"Task '{task_name}' has been added to the list.")

def show_tasks():
    """
    Display the list of tasks.
    """
    if not tasks:
        print("Your task list is empty.")
    else:
        print("\n--- TASK LIST ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task():
    """
    Remove a task from the task list.
    """
    show_tasks()  # Display tasks for user to select
    if tasks:
        try:
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' has been removed from the list.")
            else:
                print("Please enter a valid task number.")
        except ValueError:
            print("Please enter a numeric value.")

def save_tasks():
    """
    Save the task list to a JSON file.
    """
    with open('tasks.json', 'w') as file:
        json.dump({"tasks": tasks}, file)
    print("Your tasks have been saved successfully.")

def load_tasks():
    """
    Load the task list from a JSON file.
    """
    global tasks
    try:
        with open('tasks.json', 'r') as file:
            data = json.load(file)
            tasks = data["tasks"]
            print("Your tasks have been loaded successfully.")
    except FileNotFoundError:
        print("No saved file found!")

def run():
    """
    Run the To-Do List program.
    """
    while True:
        display_menu()
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                add_task()
            elif choice == 2:
                show_tasks()
            elif choice == 3:
                remove_task()
            elif choice == 4:
                save_tasks()
            elif choice == 5:
                load_tasks()
            elif choice == 6:
                print("Exiting the To-Do List. Goodbye!")
                break
            else:
                print("Please select a valid option.")
        except ValueError:
            print("Please enter a numeric value.")

