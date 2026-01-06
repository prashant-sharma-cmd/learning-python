def add_task(task_list, new_task):
    task = {"name": new_task, "completed": False}
    task_list.append(task)
    return task_list

def list_pending(task_list):
    pending = list(filter(lambda task: not task["completed"], task_list))
    return pending

def complete_all(task_list):
    updated_tasks = list(map(lambda task: {**task, "completed": True}, task_list))
    return updated_tasks

def search_tasks(task_list, keyword):
    search_result = list(filter(lambda task: keyword.lower() in task["name"], task_list))
    return search_result
