import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)
    print("Tasks saved!")


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet!")
        return
    print("\n--- Your To-Do List ---")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "✗"
        print(f"  {i}. [{status}] {task['title']}")
    print("-----------------------")


def add_task(tasks):
    title = input("Enter task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print(f'Task "{title}" added!')
    else:
        print("Task cannot be empty.")


def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f'Task "{removed["title"]}" removed!')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print(f'Task "{tasks[num - 1]["title"]}" marked as done!')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()
    print("=== To-Do List App ===")

    while True:
        print("\nWhat would you like to do?")
        print("  1. View tasks")
        print("  2. Add task")
        print("  3. Remove task")
        print("  4. Mark task as done")
        print("  5. Save tasks")
        print("  6. Quit")

        choice = input("\nEnter choice (1-6): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            save_tasks(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
