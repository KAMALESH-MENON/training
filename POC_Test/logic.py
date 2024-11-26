from db import db_connection
from employee import Employee

class Logic:
    """
    Logic part of POC_Test 
    """
    def __init__(self):
        self.connection = db_connection()

    def get_employees(self):
        """
        List all employee
            
        Return: list of employee or empty list
        """
        cursor = self.connection.execute('SELECT emp_no, emp_name, location, dept_id FROM employee')
        employees = [Employee(row[0], row[1], row[2], row[3]) for row in cursor.fetchall()]
        return employees

    def update_employee(self, update_employee):
        """
        Update the price of the given product
        
        Input: update_product (Employee object)
        
        Return: boolean
        """
        cursor = self.connection.execute(
                    'UPDATE employee SET location = ?, dept_id = ? WHERE emp_no = ?',
                    (update_employee.location, update_employee.dept_id, update_employee.emp_no)
                )
        return cursor.rowcount > 0

    def get_employee_by_emp_no(self, emp_no: int):
        """
        Check if an employee exists by employee number.
        
        input: emp_no (int) -> Employee number
            
        Return: boolean -> True if the employee exists, False otherwise.
        """
        cursor = self.connection.execute(
                    'SELECT emp_no, emp_name, location, dept_id FROM employee where emp_no = ?',
                    (emp_no,)
                )
        employee = cursor.fetchone()
        print(employee)
        if employee is None:
            return False
        else:
            return employee

    def get_employee_by_location(self, location):
        """
        get_employee_by_location
        
        input: location (string) 
            
        Return: list of employee or empty list
        """
        cursor = self.connection.execute(
                    'SELECT emp_no, emp_name, location, dept_id FROM employee where location = ? ',
                    (location,)
                )
        employees = [Employee(row[0], row[1], row[2], row[3]) for row in cursor.fetchall()]
        return employees
