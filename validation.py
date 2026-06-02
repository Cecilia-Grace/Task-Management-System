from datetime import datetime

def validate_task_title(title):
    if len(title.strip()) == 0:
        raise ValueError("Please input the task title")
    return None

def validate_task_description(description):
    if len(description.strip()) == 0:
        raise ValueError("Please input task description")
    return None

def validate_due_date(due_date):
    date_format = "%Y-%m-%d"
    
    if len(due_date.strip()) == 0:
        return "Input a due date"
    
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Enter correct date format (yyyy-mm-dd)" )   
       
    return None


