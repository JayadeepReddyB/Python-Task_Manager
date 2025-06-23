def view_task():
    print("Viewing tasks...")
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks available.")
            else:
                for task in tasks:
                    print(task.strip())
    except FileNotFoundError:
        print("No tasks file found. Please create a task first.")

def create_task():
    user = input("Enter the password to create a task: ")
    if user != "password123":
        print("Incorrect password. Task creation failed.")
        return
    print("Creating a new task...")
    task = input("Enter the task description: ")    
    with open('tasks.txt', 'a') as file:
        file.write(task + '\n')
    print("Task created successfully.")

def update_task():
    print("Updating a task...")
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks available to update.")
                return
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
        task_number = int(input("Enter the task number to update: "))
        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number. ")
            return
        new_task = input("Enter the new task description: ")
        tasks[task_number - 1] = new_task + '\n'
        with open('tasks.txt', 'w') as file:
            file.writelines(tasks)
        print("Task updated successfully.")
    except FileNotFoundError:
        print("No tasks file found. Please create a task first.")

def delete_task():
    print("Deleting a task...")

    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
            if not tasks:
                print("No taasks available to delete.: ")
                return
            for i, task in enumerate(tasks, start = 1):
                print(f"{i}. {task.strip()}")
            task_number = int(input("Enter the task number to delete: "))
            if task_number < 1 or task_number > len(tasks):
                print("Invalid task number.")
                return
            tasks.pop(task_number - 1)
        with open('tasks.txt', 'w') as file:
            file.writelines(tasks)
        print("Task deleted successfully.")
    except FileNotFoundError:
        print("No tasks file found. Please create a task first.")

def exit_task_manager():
    print("Exiting the task manager. Goodbye!")
    exit()

while True:
    choice = int(input('''
        1) View Tasks
        2) Create New Task
        3) Update Task
        4) Delete Task
        5) Exit            
    '''))

    match choice:
        case 1:
            view_task()
        case 2:
            create_task()
        case 3:
            update_task()
        case 4:
            delete_task()
        case 5:
            exit_task_manager()
        case _:
            print("Invalid Selection")

