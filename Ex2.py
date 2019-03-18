


# Exercise 2

from sys import argv

task_list = []
file = open(argv[1])

for line in file:
    task_list.append(line)

file.close()


while True:

    print("\n\nTo do manager:\n\n 1.\tinsert a new task\n 2.\tremove a task")
    print(" 3.\tshow all existing tasks\n 4.\tclose the program\n\n")

    cmd = input("Command: ")

    if cmd == "1":
        # Insert a new task

        task = input("New task: ")
        task_list.append(task+"\n")

    elif cmd == "2":
        # remove a task

        task = input("Task to be deleted: ")

        if task_list.__contains__(task+"\n"):
            task_list.remove(task+"\n")
        else:
            print("Task %s is not in the list" % task)

    elif cmd == "3":
        # Show existing tasks

        print("To do list:\n")
        for task in sorted(task_list):
            print(task, end="")

    elif cmd == "4":
        # Close

        file = open(argv[1], 'w')
        for task in task_list:
            file.write(task)
        break

    else:
        # Default
        print("\nUnknown command %s\n\n" % cmd)
