from logic import Logic
from employee import Employee

def main():
    l1 = Logic()

    # Adding employees for testing
    emp1 = Employee(1, "John Doe", "New York", 101)
    emp2 = Employee(2, "Jane Smith", "Los Angeles", 102)
    emp3 = Employee(3, "Bob Johnson", "Chicago", 103)
    
    # Insert employees into database
    l1.connection.execute('INSERT OR REPLACE INTO employee (emp_no, emp_name, location, dept_id) VALUES (?, ?, ?, ?)',
                          (emp1.emp_no, emp1.emp_name, emp1.location, emp1.dept_id))
    l1.connection.execute('INSERT OR REPLACE INTO employee (emp_no, emp_name, location, dept_id) VALUES (?, ?, ?, ?)',
                          (emp2.emp_no, emp2.emp_name, emp2.location, emp2.dept_id))
    l1.connection.execute('INSERT OR REPLACE INTO employee (emp_no, emp_name, location, dept_id) VALUES (?, ?, ?, ?)',
                          (emp3.emp_no, emp3.emp_name, emp3.location, emp3.dept_id))
    l1.connection.commit()

    # Get and print all employees
    print("All Employees:")
    employees = l1.get_employees()
    for emp in employees:
        print(emp)

    # Update an employee
    emp_update = Employee(2, "Jane Smith", "San Francisco", 104)
    update_status = l1.update_employee(emp_update)
    print("\nUpdate Status for Jane Smith:", "Successful" if update_status else "Failed")

    # Get employee by employee number
    print("\nGet Employee by Emp No (2):")
    emp = l1.get_employee_by_emp_no(2)
    if emp:
        print(emp)
    else:
        print("Employee not found")

    # Get employee by location
    print("\nGet Employees by Location (Chicago):")
    employees_by_location = l1.get_employee_by_location("Chicago")
    for emp in employees_by_location:
        print(emp)

if __name__ == "__main__":
    main()
