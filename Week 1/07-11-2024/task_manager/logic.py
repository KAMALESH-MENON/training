def delete_task(task_id, tasks):
    for i in range(len(tasks)):
        if tasks[i]['taskId'] == task_id:
            del tasks[i]
            break


def running_task(tasks):
    for task in tasks:
        if task["status"] == "running":
            print(f"taskId : {task["taskId"]}, status : {task["status"]}")
    
def update_task(task_id, status, tasks):
    for task in tasks:
        if task["taskId"] == task_id:
            task["status"] = status
            break
        

def display_task(tasks):
    for task in tasks:
        print(f"taskId: {task["taskId"]} , status: {task["status"]}")
        
        
def add_task(taskId, status, tasks):
    temp_dict = {"taskId": taskId, "status": status}
    tasks.append(temp_dict)
    print("\nAdded Task\n")
    