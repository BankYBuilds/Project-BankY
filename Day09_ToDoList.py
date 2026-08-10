tasks = {
    1: {"task": "Study Python", "completed": False},
    2: {"task": "Build a project", "completed": False}
}

print("1. View tasks")
print("2. Add task")
print("3. Mark task as completed")
print("4. Exit")


while True:
    choice = input("Choose an option: ")

    print(choice)

    if choice == "1":
        for id, task in tasks.items():
            status = "Completed" if task["completed"] else "Not completed"
            print(f"{id}: {task['task']} - {status}")

    elif choice == "2":
        task_id = int(input("Enter the task number: "))
        add_task = input("What task do you want to add?:\n")
        tasks[task_id] = {
    "task": add_task,
    "completed": False
}
        print(tasks)

    elif choice == "3":
        task_id = int(input("Enter the task number: "))

        if task_id in tasks:
            tasks[task_id]["completed"] = True
            print("Task marked as completed")
        else:
            print("Task not found.")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid option.")