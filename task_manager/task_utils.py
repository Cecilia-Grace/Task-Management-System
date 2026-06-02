from datetime import datetime
# Import validation functions
from task_manager.validation import validate_due_date, validate_task_description, validate_task_title

# Define tasks list
tasks = []
# Implement add_task function
def add_task(title, description, due_date):
    title_error = validate_task_title(title)
    description_error = validate_task_description(description)
    due_date_error = validate_due_date(due_date)
    
    if title_error:
        return title_error
    
    if description_error:
        return description_error
    
    if due_date_error:
        return due_date_error
    
    new_task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    
    tasks.append(new_task)

    return "Task added successfully!"
    
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    target_task = tasks[index]
    
    target_task["completed"] = True
        
    return f"{target_task['title']} has been marked as complete"

# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    is_pending = False
    
    for task in tasks:
        if task["completed"] == False:
            print(f"{task['title']} - {task['completed']}")
            is_pending = True
    
    if is_pending == False:
        print("No pending tasks")
    

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if not tasks:
        return "No tasks available"
    
    completed_tasks = 0
    uncompleted_tasks = 0
    
    for task in tasks:
        if task["completed"] == True:
            completed_tasks +=1
        else:
            uncompleted_tasks +=1
   
    return f"Completed tasks: {completed_tasks}|| Uncompleted tasks: {uncompleted_tasks}"
