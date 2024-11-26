import csv
from io import StringIO
from typing import List

from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from .models import Employee, User
from .schemas import EmployeeCreate, EmployeeRead, SearchRequest, UserLogin


def authenticate_user(user: UserLogin, db: Session):
    """
    Authenticates a user by checking the provided credentials.

    Input:
        user (UserLogin): The user credentials.
        db (Session): The database session.

    Returns: 
        dict: A message indicating the login status.
    Raises: 
        HTTPException: If the user id or password is incorrect.
    """
    db_user = db.query(User).filter(User.user_id == user.user_id).first()
    if db_user is None or db_user.password != user.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user id or password",
        )
    return {"message": "Login successful"}


def create_user(user: UserLogin, db: Session):
    """
    Creates a new user in the database. 

    Input:
        user (UserLogin): The user details to create. 
        db (Session): The database session. 

    Returns: 
        dict: A message indicating the user registration status. 

    Raises: 
        HTTPException: If the user id already exists. 
    """
    try:
        db_user = User(user_id=user.user_id, password=user.password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return {"message": "User Registered"}
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User id already exists"
        ) from exc


def add_employee(employee: EmployeeCreate, db: Session):
    """
    Creates a new employee in the database.

    Input:
        employee (EmployeeCreate): The employee details to create.
        db (Session): The database session.

    Returns: 
        EmployeeRead:The created employee. 

    Raises:
        HTTPException: If the employee already exists or if there is a database error.
    """
    try:
        db_employee = Employee(
            firstname=employee.firstname,
            lastname=employee.lastname,
            date_of_birth=employee.date_of_birth,
            date_of_joining=employee.date_of_joining,
            grade=employee.grade,
        )
        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)
        return db_employee
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Employee already exists"
        ) from exc
    except SQLAlchemyError as exc:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(exc)}",
        ) from exc


def get_all_employees(db: Session):
    """
    Retrieves all employees from the database.

    Input:
        db (Session): The database session.

    Returns:
        List[EmployeeRead]: A list of all employees.

    Raises: HTTPException: If there is a database error.
    """
    try:
        return db.query(Employee).all()
    except SQLAlchemyError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Database error: {str(exc)}'
        ) from exc


def search_employees(search_request: SearchRequest, db: Session) -> List[EmployeeRead]:
    """
    Searches for employees based on a key and value.
    
    Input:
        search_request (SearchRequest): The search key and value.
        db (Session): The database session.

    Returns:
        List[EmployeeRead]: A list of employees matching the search criteria.

    Raises:
        HTTPException: If the search key is invalid or if there is a database error.
    """
    key = search_request.key
    value = search_request.value

    try:
        if key == "firstname":
            return db.query(Employee).filter(Employee.firstname.ilike(f"%{value}%")).all()
        elif key == "lastname":
            return db.query(Employee).filter(Employee.lastname.ilike(f"%{value}%")).all()
        elif key == "grade":
            return db.query(Employee).filter(Employee.grade == value).all()
        elif key == "employee_id":
            return db.query(Employee).filter(Employee.employee_id == value).all()
        elif key == "date_of_birth":
            return db.query(Employee).filter(Employee.date_of_birth == value).all()
        elif key == "date_of_joining":
            return db.query(Employee).filter(Employee.date_of_joining == value).all()
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid search key"
                )
    except SQLAlchemyError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(SQLAlchemyError)}"
            ) from exc


def update_employee(employee_id: int, employee: EmployeeCreate, db: Session):
    """
    Updates an employee's details based on the provided employee ID.

    Input:
        employee_id (int): The ID of the employee to update.
        employee (EmployeeCreate): The employee details to update.
        db (Session): The database session.

    Returns: 
        EmployeeRead: The updated employee. 
    
    Raises: 
        HTTPException: If the employee is not found or if there is a database error.
    """
    try:
        db_employee = (
            db.query(Employee).filter(Employee.employee_id == employee_id).first()
        )
        if db_employee is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found"
            )

        if hasattr(employee, "firstname") and employee.firstname is not None:
            db_employee.firstname = employee.firstname
        if hasattr(employee, "lastname") and employee.lastname is not None:
            db_employee.lastname = employee.lastname
        if hasattr(employee, "date_of_birth") and employee.date_of_birth is not None:
            db_employee.date_of_birth = employee.date_of_birth
        if (hasattr(employee, "date_of_joining") and employee.date_of_joining is not None):
            db_employee.date_of_joining = employee.date_of_joining
        if hasattr(employee, "grade") and employee.grade is not None:
            db_employee.grade = employee.grade

        db.commit()
        db.refresh(db_employee)
        return db_employee

    except SQLAlchemyError as exc:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(exc)}",
        ) from exc



def bulk_create_employees_from_csv(file: StringIO, db: Session):
    """
    Creates employees from a CSV file.

    Input:
        file (StringIO): The CSV file containing employee data.
        db (Session): The database session.

    Returns:
        List[EmployeeRead]: A list of created employees.
    
    Raises: HTTPException: If there is an error processing the CSV file.
    """
    try:
        reader = csv.DictReader(file)
        employees = []
        for row in reader:
            employee_data = EmployeeCreate(**row)
            db_employee = Employee(
                firstname=employee_data.firstname,
                lastname=employee_data.lastname,
                date_of_birth=employee_data.date_of_birth,
                date_of_joining=employee_data.date_of_joining,
                grade=employee_data.grade,
            )
            db.add(db_employee)
            db.commit()
            db.refresh(db_employee)
            employees.append(db_employee)
        return employees
    except Exception as exc:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error processing CSV file",
        ) from exc


def export_employees_to_csv(db: Session) -> str:
    """
    Exports all employees to a CSV file.

    Input:
        db (Session): The database session.

    Returns:
        str: The CSV content as a string.

    Raises:
        HTTPException: If there are no employees found or if there is a database error.
    """
    try:
        employees = db.query(Employee).all()
        if not employees:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="No employees found"
            )

        output = StringIO()
        writer = csv.writer(output)

        # Write CSV headers
        writer.writerow(
            [
                "employee_id",
                "firstname",
                "lastname",
                "date_of_birth",
                "date_of_joining",
                "grade",
            ]
        )

        # Write CSV rows
        for employee in employees:
            writer.writerow(
                [
                    employee.employee_id,
                    employee.firstname,
                    employee.lastname,
                    employee.date_of_birth.strftime("%Y-%m-%d"),
                    employee.date_of_joining.strftime("%Y-%m-%d"),
                    employee.grade,
                ]
            )

        return output.getvalue()
    except SQLAlchemyError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(exc)}",
        ) from exc
