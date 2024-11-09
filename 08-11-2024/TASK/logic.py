class Logic:
    def __init__(self):
        self.tasks = []

    def view_all(self):
        return self.tasks

    def add(self, task):
        for t in self.tasks:
            if t.task_id == task.task_id:
                return False
        self.tasks.append(task)
        return True

    def update(self, task):
        for t in self.tasks:
            if task.task_id == t.task_id:
                t.status = task.status
                t.location = task.location
                t.priority = task.priority
                return True
        return False

    # def update(self, taskid, status, priority, location):
        # for t in self.tasks:
        #     if t.task_id == taskid:
        #         t.status = status
        #         t.priority = priority
        #         t.location = location
        #         return True
        # return False



    def view_task_by_loaction(self, location):
        location_list = []
        for task in self.tasks:
            if task.location == location:
                location_list.append(task)
        if location_list:
            return location_list
        return False


    def view_status_running(self):
        running_list = []
        for task in self.tasks:
            if task.status == "Running":
                running_list.append(task)
        if running_list:
            return running_list
        return False

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return True
        return False
        # for i in range(len(self.tasks)):
        #     if self.tasks[i].task_id == taskid:
        #         del self.tasks[i]
        #         self.tasks.remove()
        #         return True
        # return False
