from datetime import datetime

def validate_task_title(title):
    if not title:
        return "Please input the task title"
    return None

def validate_task_description(description):
    if not description:
        return "Please input task description"
    return None

def validate_due_date(due_date):
    date_format = "%Y-%m-%d"
    today = datetime.today().date()
    
    if not due_date:
        return "Input a due date"
    
    try:
        parsed_date = datetime.strptime(due_date, date_format).date()
    except ValueError:
        return "Enter correct date format (yyyy-mm-dd)" 
       
    if parsed_date < today:
        return "Cannot enter past date"
    
    return None


