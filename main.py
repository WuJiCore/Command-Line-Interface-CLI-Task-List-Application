# Initialize an empty list to store the tasks
task_list = []

def show_menu():
    """Displays the main application menu."""
    print("\n--- Wu-Ji Core CLI To-Do ---")
    print("1. View To-Do List")
    print("2. Add New Task")
    print("3. Delete Task")
    print("4. Exit")
    print("---------------------------")

def view_tasks():
    """Displays all tasks in the list."""
    print("\n--- Your To-Do List ---")
    if not task_list:
        print("No tasks yet. Let's add a new one!")
    else:
        for i, task in enumerate(task_list, start=1):
            print(f"{i}. {task}")
    print("-------------------------")

def add_task():
    """Adds a new task to the list."""
    new_task = input("Enter a new task: ")
    if new_task.strip(): # Ensure the input is not empty
        task_list.append(new_task)
        print(f"'{new_task}' has been added successfully!")
    else:
        print("Task cannot be empty.")

def delete_task():
    """Deletes a task from the list based on its number."""
    view_tasks()
    if not task_list:
        return # Exit if the list is empty

    try:
        task_number = int(input("Enter the number of the task to delete: "))
        if 1 <= task_number <= len(task_list):
            deleted_task = task_list.pop(task_number - 1)
            print(f"'{deleted_task}' has been deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number only.")

# Main Program
if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Select an option (1-4): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Thank you for using Wu-Ji Core CLI To-Do. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
