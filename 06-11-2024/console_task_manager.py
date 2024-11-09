def delete_task(task_id):
    for i in range(len(tasks)):
        if tasks[i]['taskId'] == task_id:
            del tasks[i]
            break


def running_task():
    for task in tasks:
        if task["status"] == "running":
            print(f"taskId : {task["taskId"]}, status : {task["status"]}")
    
def update_task(task_id, status):
    for task in tasks:
        if task["taskId"] == task_id:
            task["status"] = status
            break
        

def display_task():
    for task in tasks:
        print(f"taskId: {task["taskId"]} , status: {task["status"]}")
        
        
def add_task(taskId, status):
    temp_dict = {"taskId": taskId, "status": status}
    tasks.append(temp_dict)
    print("\nAdded Task\n")
    

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
        add_task(taskId, status)
    
    elif choice == 2:
        taskId = int(input("Enter the taskId : "))
        status = input("Enter the status : ")
        update_task(taskId, status)
        print("\nUpdated Task\n")
        
    elif choice == 3:
        taskId = int(input("Enter the taskId : "))
        delete_task(taskId)
        print("\nDeleted Task\n")
        
    
    elif choice == 4:
        display_task()
        
    elif choice == 5:
        running_task()
    
    choice = int(input("Enter your choice : "))
    

