tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter Task: ")
        tasks.append(task)
        print("Task Added Successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No Tasks Available!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No Tasks Available!")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            num = int(input("Enter task number to remove: "))
            tasks.pop(num - 1)
            print("Task Removed Successfully!")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")