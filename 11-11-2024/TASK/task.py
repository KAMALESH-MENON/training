class Task:
    def __init__(self, task_id, task_name, status, priority, location):
        self.task_id = task_id
        self.task_name = task_name
        self.status = status
        self.priority = priority
        self.location = location

    def __str__(self):
        return (f"Task id: {self.task_id}, Task Name: {self.task_name}, Status: {self.status}, Priority: {self.priority}, Location: {self.location}")