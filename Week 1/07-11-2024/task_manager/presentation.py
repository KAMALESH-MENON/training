import logic

def print_menu():
    print("\n1. Add Task. -- ask for tasked and status and add to the list... a new dictionary\n2. update Task  -- ask for tasked and ask for status and change status alone\n3. Remove Task. -- ask for tasked and remove the dictionary from the List]\n4. print All Tasks and status.  -- print each task and its status.\n5. print only running tasks.  -- print only tasked where status is running\n0. exit\n")


tasks = []

print_menu()  
choice = int(input("Enter your choice : "))
while(choice != 0):
    if choice == 0:
        break
    elif choice == 1:
        taskId = int(input("Enter the taskId : "))
        status = input("Enter the status : ")
        logic.add_task(taskId, status, tasks)
    
    elif choice == 2:
        taskId = int(input("Enter the taskId : "))
        status = input("Enter the status : ")
        logic.update_task(taskId, status, tasks)
        print("\nUpdated Task\n")
        
    elif choice == 3:
        taskId = int(input("Enter the taskId : "))
        logic.delete_task(taskId, tasks)
        print("\nDeleted Task\n")
        
    
    elif choice == 4:
        logic.display_task(tasks)
        
    elif choice == 5:
        logic.running_task(tasks)
    
    choice = int(input("Enter your choice : "))
    
