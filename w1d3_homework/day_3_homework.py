from optparse import Values


tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# 1. Print a list of uncompleted tasks
def uncompleted_task():
    for task in tasks:
        if task ["completed"] == False:
            print(task)
uncompleted_task()

# 2.Print a list of completed tasks
def completed_task():
    for task in tasks:
        if task ["completed"] == True:
            print(task)
completed_task()

# 3.Print a list of all task descriptions
def all_task_description():
    for task in tasks:
        print(task["description"])
all_task_description()

# 4.Print a list of tasks where time_taken is at least a given time
def slow_task(min_time_taken):
    for task in tasks:
        if task ["time_taken"] > min_time_taken:
            print(task)
slow_task(7)
    
# 5.Print any task with a given description    
def print_one_task(description):
    for task in tasks:
        if task ["description"] == description:
            print(task)
print_one_task("Feed Cat")

# 6. Given a description update that task to mark it as complete.
# Errors:
# def mark_task_as_complete(description):
#     for task in tasks:
#         if ["completed"] == False:
#             ["completed"] = True
#         elif ["completed"] == True:
#             print(task)
# mark_task_as_complete("Wash Dishes")

# This doesn't work, but no errors:
# def mark_task_as_complete(description):
#     for task in tasks:
#         if task == False:
#             task = True
#         elif task == True:
#             print(task)
# mark_task_as_complete("Wash Dishes")

# Errors:
# def mark_task_as_complete(description):
#     for task in tasks:
#         if task[0]["completed"] == True:
#             print(task)
#     else:
#         print(task[0]["completed"] == True)
# mark_task_as_complete("Wash Dishes")

# 7.Add a task to the list
tasks.append({
    "description" : "Bake dessert", "completed" : True, "time_taken" : 40
})
print(tasks)




