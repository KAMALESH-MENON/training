class Employee:
    def __init__(self, emp_no, emp_name, location, dept_id):
        self.emp_no = emp_no
        self.emp_name = emp_name
        self.location = location
        self.dept_id = dept_id

    def __str__(self):
        return f"emp_no: {self.emp_no}, emp_name: {self.emp_name}, location: {self.location}, dept_id: {self.dept_id}"
