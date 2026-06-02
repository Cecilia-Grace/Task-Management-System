# Import functions from task_manager.task_utils package
from task_manager.task_utils import add_task, view_pending_tasks, mark_task_as_complete, tasks, calculate_progress

task = {"title": "Groceries",
        "description": "Shop at Market Basket for food", 
        "due_date": "2024-06-26",
        "completed": True
        }

# Define the main function
def main():
    
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            
            add_task_result = add_task(title, description, due_date)
            print(add_task_result)

            
        elif choice == "2":
            # view_pending_tasks(tasks)
            user_input = input("Task: ")
                   
            if not user_input:
                print("Enter an index")
                continue
            
            if user_input.isdigit():
                selected_task = int(user_input) -1
                
                if selected_task >= len(tasks) or selected_task < 0:
                    print("Enter a valid index")
                    continue
                
                marked_result = mark_task_as_complete(selected_task)
                print(marked_result)
                
                
        elif choice == "3":
            view_pending_tasks(tasks)
            
        elif choice == "4":
            progress_result = calculate_progress(tasks)
            print(progress_result)
            
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
        
        
        
if __name__ == "__main__":
    main()
