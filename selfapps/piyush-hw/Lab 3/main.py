from functions import *
tasks = []
while True:
    action = input("Enter:\na : Adding new task\n"
                   "f : Filter incomplete tasks\n"
                   "m : Mark all tasks completed\n"
                   "s : Search a task\n")

    if action == "a":
        new_task = input("Enter the new task: ")
        tasks = add_task(tasks, new_task)
        print("Task added successfully!")

    if action == "f":
        pending = list_pending(tasks)
        print("List of pending tasks are:\n")
        for item in pending:
            print(item["name"]+"\n")

    if action == "m":
        tasks = complete_all(tasks)
        print("All tasks completed!")

    if action == "s":
        search_keyword = input("Enter the keyword to search for: ")
        search_result = search_tasks(tasks, search_keyword)
        print("Tasks found:\n")
        if search_result:
            for item in search_result:
                print(item["name"]+"\n")
        else:
            print("None.")
