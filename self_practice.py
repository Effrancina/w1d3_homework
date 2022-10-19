tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# # 1. Print a list of uncompleted tasks
# def uncompleted_task():
#     for task in tasks:
#         if task ["completed"] == False:
#             print(task)
# uncompleted_task()

# # 2.Print a list of completed tasks
# def completed_task():
#     for task in tasks:
#         if task ["completed"] == True:
#             print(task)
# completed_task()

# # 3.Print a list of all task descriptions
# def all_task_description():
#     for task in tasks:
#         print(task["description"])
# all_task_description()

# # 4.Print a list of tasks where time_taken is at least a given time
# def slow_task(min_time_taken):
#     for task in tasks:
#         if task ["time_taken"] > min_time_taken:
#             print(task)
# slow_task(7)
    
# # 5.Print any task with a given description    
# def print_one_task(description):
#     for task in tasks:
#         if task ["description"] == description:
#             print(task)
# print_one_task("Feed Cat")

# 6. Given a description update that task to mark it as complete.

def mark_task_as_complete(description):
    for task in tasks:
        task[0]["completed"][True]
    else:
        print(tasks[0]["completed"].update("completed_1"))
mark_task_as_complete("Wash Dishes")



# d.update(d1)


# 7. Add a task to the list









