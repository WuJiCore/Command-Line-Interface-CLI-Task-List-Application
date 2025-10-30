# Wu-Ji Core CLI To-Do

*A simple command-line (CLI) To-Do List application to manage your daily tasks.*

**Official by Wu-Ji Core**

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)

## Description

Wu-Ji Core CLI To-Do is a very lightweight and easy-to-use Python program. Without a complex interface, you can quickly add, view, and delete your to-do items directly from your terminal or command prompt. This project is perfect for beginners who want to learn the basics of Python programming and how Git/GitHub works.

## Features

- ✨ **View To-Do List**: Display all tasks you have added.
- ➕ **Add New Task**: Easily add a new task.
- ❌ **Delete Task**: Remove tasks that are completed or no longer needed.
- 🚀 **Lightweight & Fast**: Runs directly in the terminal without any additional dependencies.
- 📚 **Easy to Learn**: The source code is written clearly with full documentation for learning purposes.

## Installation & Running

**Prerequisites:**
Make sure you have Python 3 installed on your computer. You can check by running the command `python --version` or `python3 --version` in your terminal.

**Steps:**

1.  **Clone this repository** to your computer:
    ```bash
    git clone https://github.com/your-username/wuji-todo-cli.git
    ```
    (Replace `your-username` with your GitHub username)

2.  **Navigate to the project folder:**
    ```bash
    cd wuji-todo-cli
    ```

3.  **Run the program:**
    ```bash
    python main.py
    ```
    Or if the command above doesn't work, try:
    ```bash
    python3 main.py
    ```

## How to Use

Once the program is running, you will see the main menu. Simply enter the number corresponding to the menu you want and press Enter.

- **Select 1**: To view all existing tasks.
- **Select 2**: To add a new task. You will be prompted to enter the task description.
- **Select 3**: To delete a task. The program will show the list of tasks with their numbers, and you can enter the number of the task you want to delete.
- **Select 4**: To exit the program.

---

## Code Explanation (`main.py`)

Here is a detailed explanation of each part of the code in `main.py` to make it easy to understand.

### 1. Initialization and Menu Function

```python
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
```
- `task_list = []`: We create a variable named `task_list` with an empty list (or array) data type. This list will be used to store all the task strings entered by the user.
- `def show_menu()`: This is a function definition. This function's job is to print the menu options to the screen so the user knows what they can do. Separating it into a function makes the code cleaner and can be called repeatedly.

### 2. The `view_tasks()` Function

```python
def view_tasks():
    """Displays all tasks in the list."""
    print("\n--- Your To-Do List ---")
    if not task_list:
        print("No tasks yet. Let's add a new one!")
    else:
        for i, task in enumerate(task_list, start=1):
            print(f"{i}. {task}")
    print("-------------------------")
```
- `if not task_list:`: This is a conditional check. If the `task_list` is empty, the program will print the message "No tasks yet".
- `else:`: If the list is not empty, this block of code will be executed.
- `for i, task in enumerate(task_list, start=1):`: This is a `for` loop.
  - `enumerate()` is a very useful built-in Python function. It will iterate (look one by one) at the items inside `task_list` and give us two things: the **index** (stored in the variable `i`) and its **value** (stored in the variable `task`).
  - `start=1` means we want the index count to start from 1, not 0 (Python's default), to be more user-friendly.
- `print(f"{i}. {task}")`: This is an f-string. A modern and easy way to format strings in Python. It will print the sequence number and the task.

### 3. The `add_task()` Function

```python
def add_task():
    """Adds a new task to the list."""
    new_task = input("Enter a new task: ")
    if new_task.strip(): # Ensure the input is not empty
        task_list.append(new_task)
        print(f"'{new_task}' has been added successfully!")
    else:
        print("Task cannot be empty.")
```
- `new_task = input(...)`: The `input()` function waits for the user to type something and press Enter. What is typed will be stored as a string in the `new_task` variable.
- `if new_task.strip():`: `.strip()` is a string method that removes spaces from the beginning and end of a string. This condition ensures that the user doesn't just type empty spaces.
- `task_list.append(new_task)`: `.append()` is a list method that adds a new element (`new_task`) to the end of the list.

### 4. The `delete_task()` Function

```python
def delete_task():
    # ... (see code above) ...
    try:
        task_number = int(input("Enter the number of the task to delete: "))
        if 1 <= task_number <= len(task_list):
            deleted_task = task_list.pop(task_number - 1)
            print(f"'{deleted_task}' has been deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number only.")
```
- `try...except`: This is an *error handling* block. We "try" (`try`) to run code that has the potential for error (e.g., the user inputs letters instead of numbers). If a `ValueError` occurs (an error because the input cannot be converted to a number), the program won't crash, but will instead run the code in the `except` block.
- `int(input(...))`: We convert the user's input (which is originally a string) into an integer (a whole number).
- `if 1 <= task_number <= len(task_list):`: We check if the number entered by the user is within a valid range (between 1 and the total number of tasks).
- `task_list.pop(task_number - 1)`: `.pop()` is a list method that removes an element based on its index. We subtract 1 because Python lists start at index 0, while the user sees numbers starting from 1.

### 5. Main Program

```python
if __name__ == "__main__":
    while True:
        # ... (code inside the while loop) ...
```
- `if __name__ == "__main__":`: This is a standard in Python. The code inside this block will only run if this file is executed directly (e.g., with `python main.py`), not when it's imported as a module.
- `while True:`: This is an *infinite loop*. The program will keep running and displaying the menu until the user chooses to exit.
- `if/elif/else`: This structure checks the choice entered by the user (`'1'`, `'2'`, etc.) and runs the corresponding function.
- `break`: If the user chooses '4', the `break` command will stop the `while True` loop, ending the program.

---

## Contributing

Your contributions are highly appreciated! If you have ideas for new features or find a bug, please do the following:

1.  *Fork* this repository.
2.  Create a new branch (`git checkout -b feature-new`).
3.  *Commit* your changes (`git commit -am 'Add feature X'`).
4.  *Push* to the new branch (`git push origin feature-new`).
5.  Create a *Pull Request*.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Developed with ❤️ by **Wu-Ji Core**
