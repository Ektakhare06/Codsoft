import json
import os

# Load tasks from file if exists
def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)

# Add a new task
def add_task(tasks):
    task = input("Enter the new task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added!")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks in your to-do list.")
    else:
        for i, task in enumerate(tasks):
            status = "✓" if task['completed'] else "✗"
            print(f"{i + 1}. {task['task']} [{status}]")

# Update task status
def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to mark complete: ")) - 1
        tasks[task_number]['completed'] = True
        print(f"Task '{tasks[task_number]['task']}' marked as complete!")
    except (IndexError, ValueError):
        print("Invalid task number!")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to delete: ")) - 1
        removed_task = tasks.pop(task_number)
        print(f"Task '{removed_task['task']}' deleted!")
    except (IndexError, ValueError):
        print("Invalid task number!")

# Main application loop
def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
