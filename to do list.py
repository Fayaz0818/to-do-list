def display_todo_list(todo_list):
    if todo_list:
        print("To-Do List:")
        for index, task_info in enumerate(todo_list, 1):
            print(f"{index}. {task_info[0]} ({task_info[1]})")
    else:
        print("Your to-do list is empty.")

def mark_task_completed(todo_list):
    if todo_list:
        display_todo_list(todo_list)
        task_number = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_number <= len(todo_list):
            todo_list[task_number - 1] = (todo_list[task_number - 1][0], "Done")
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number. Please enter a valid task number.")
    else:
        print("Your to-do list is empty.")

def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append((task, "Not Done"))
    print(f"Task '{task}' added to your to-do list.")

def remove_task(todo_list):
    if todo_list:
        display_todo_list(todo_list)
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(todo_list):
            task = todo_list.pop(task_number - 1)
            print(f"Task '{task[0]}' removed from your to-do list.")
        else:
            print("Invalid task number. Please enter a valid task number.")
    else:
        print("Your to-do list is empty.")
        task_number = input("Enter the task number to remove: ")
        print("Invalid task number. Please enter a valid task number.")

def main():
    todo_list = []
    while True:
        print("\nOptions:")
        print("1. Display to-do list")
        print("2. Add a task")
        print("3. Mark a task as completed")
        print("4. Remove a task")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            mark_task_completed(todo_list)
        elif choice == '4':
            remove_task(todo_list)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if _name_ == "__main__":
    main()
