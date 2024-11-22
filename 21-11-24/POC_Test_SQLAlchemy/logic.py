from sqlalchemy.orm import Session
from config import SessionLocal
from employee import Employee

class Logic:
    """
    Logic part of POC_Test 
    """
    def __init__(self):
        self.db = SessionLocal()

    def get_employees(self):
        """
        List all employees
            
        Return: list of employees or empty list
        """
        return self.db.query(Employee).all()

    def update_employee(self, update_employee):
        """
        Update the location and department ID of the given employee
        
        Input: update_employee (Employee object)
        
        Return: boolean
        """
        db_employee = self.db.query(Employee).filter(Employee.emp_no == update_employee.emp_no).first()
        if db_employee:
            db_employee.location = update_employee.location
            db_employee.dept_id = update_employee.dept_id
            self.db.commit()
            return True
        return False

    def get_employee_by_emp_no(self, emp_no: int):
        """
        Check if an employee exists by employee number.
        
        input: emp_no (int) -> Employee number
            
        Return: Employee object or None
        """
        return self.db.query(Employee).filter(Employee.emp_no == emp_no).first()

    def get_employee_by_location(self, location: str):
        """
        Get employees by location
        
        input: location (string) 
            
        Return: list of employees or empty list
        """
        return self.db.query(Employee).filter(Employee.location == location).all()
