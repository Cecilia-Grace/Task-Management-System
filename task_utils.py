from datetime import datetime
# Import validation functions
from validation import validate_due_date, validate_task_description, validate_task_title

# Define tasks list
tasks = []
# Implement add_task function
def add_task(title, description, due_date):
    try:
        validate_task_title(title)
        validate_task_description(description)
        validate_due_date(due_date)
        
    except ValueError as e:
        return str(e)
    
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
        
    return "Task marked as complete!"

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
    if len(tasks) == 0:
        return "No tasks available"
    
    completed_tasks = 0
    uncompleted_tasks = 0
    
    for task in tasks:
        if task["completed"] == True:
            completed_tasks +=1
        else:
            uncompleted_tasks +=1
    
    progress = (completed_tasks/len(tasks)) * 100
   
    return progress
