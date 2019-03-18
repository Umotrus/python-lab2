


# Exercise 3

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
        to_be_removed = []

        for element in task_list:
            if task in element:
                to_be_removed.append(element)

        if to_be_removed.__sizeof__() == 0:
            print("Task %s is not in the list" % task)
        else:
            for element in to_be_removed:
                task_list.remove(element)

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
