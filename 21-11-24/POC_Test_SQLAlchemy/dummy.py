from sqlalchemy.orm import Session
from config import get_db, engine, Base, SessionLocal
from logic import Logic
from employee import Employee

def main():
    # Create tables
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    l1 = Logic()

    # Adding employees for testing
    emp1 = Employee(emp_no=1, emp_name="John Doe", location="New York", dept_id=101)
    emp2 = Employee(emp_no=2, emp_name="Jane Smith", location="Los Angeles", dept_id=102)
    emp3 = Employee(emp_no=3, emp_name="Bob Johnson", location="Chicago", dept_id=103)

    # Insert employees into database
    db.add(emp1)
    db.add(emp2)
    db.add(emp3)
    db.commit()

    # Get and print all employees
    print("All Employees:")
    employees = l1.get_employees()
    for emp in employees:
        print(emp)

    # Update an employee
    emp_update = Employee(emp_no=2, emp_name="Jane Smith", location="San Francisco", dept_id=104)
    update_status = l1.update_employee(emp_update)
    print("\nUpdate Status for Jane Smith:", "Successful" if update_status else "Failed")

    # Get employee by employee number
    print("\nGet Employee by Emp No (2):")
    emp = l1.get_employee_by_emp_no(2)
    if emp:
        print(emp)
    else:
        print("Employee not found")

    # Get employees by location
    print("\nGet Employees by Location (Chicago):")
    employees_by_location = l1.get_employee_by_location("Chicago")
    for emp in employees_by_location:
        print(emp)

if __name__ == "__main__":
    main()
