from task import Task
from logic import Logic

if __name__ == "__main__":
    T1 =  Task(1, "task 1", "Running", "Priority 1", "Coimbatore")
    T2 =  Task(2, "task 2", "Running", "Priority 1", "Coimbatore")

    L1 = Logic()

    L1.add(T1)
    L1.add(T2)

    """
    if status:
        print("Added Successfully")
    else:
        print("Not Added")
    """
    #update_status = L1.update(2, "Stopped", "Priority 5", "Chennai")
    Temp =  Task(2, "task 21", "Running fast", "Priority 5", "CBE")
    update_status = L1.update(Temp)
    print(update_status)
    # if update_status:
    #     print("Updated Successfully")
    # else:
    #     print("taskId Does not exist")

    """
    view_status_running_status = L1.view_status_running()
    if view_status_running_status:
        print("Running are : ")
        for running in view_status_running_status:
            print(running)
    else:
        print("No running task")

    delete_status = L1.delete_task(T2)
    if delete_status:
        print("Deleted task Successfully")
    else:
        print("Not Deleted")
"""
    tasks_list = L1.view_all()
    for task in tasks_list:
        print(task)
