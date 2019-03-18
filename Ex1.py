

# Exercise 1

task_list = []

while True:

    print("\n\nTo do manager:\n\n 1.\tinsert a new task\n 2.\tremove a task\n")
    print(" 3.\tshow all existing tasks\n 4.\tclose the program\n\n")

    cmd = input("Command: ")

    if cmd == "1":
        # Insert a new task

        task = input("New task: ")
        task_list.append(task)

    elif cmd == "2":
        # remove a task

        task = input("Task to be deleted: ")

        if task_list.__contains__(task):
            task_list.remove(task)
        else:
            print("Task %s is not in the list" % task)

    elif cmd == "3":
        # Show existing tasks in alphabetical order

        print("To do list: %s" % sorted(task_list))
    elif cmd == "4":
        # Close
        break

    else:
        # Default
        print("\nUnknown command %s\n\n" % cmd)
