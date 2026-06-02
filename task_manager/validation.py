from datetime import datetime

def validate_task_title(title):
    if title is None or len(title.strip()) == 0:
        return "Please input the task title"
    return None

def validate_task_description(description):
    if description is None or len(description.strip()) == 0:
        return "Please input task description"
    return None

def validate_due_date(due_date):
    date_format = "%Y-%m-%d"
    
    if due_date is None or len(due_date.strip()) == 0:
        return "Input a due date"
    
    datetime.strptime(due_date, date_format)
    
       
    return None


