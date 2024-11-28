from typing import List
import csv

from fastapi import Depends, FastAPI, File, Response, UploadFile
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .logic import (add_employee, authenticate_user,
                    bulk_create_employees_from_csv, create_user,
                    export_employees_to_csv, get_all_employees,
                    search_employees, update_employee)
from .schemas import (EmployeeCreate, EmployeeRead,
                      SearchRequest, UserLogin)

app = FastAPI()
security = HTTPBasic()

Base.metadata.create_all(bind=engine)

# Register a new user
@app.post("/register", tags=["login"])
def register(user: UserLogin, db: Session = Depends(get_db)):
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
    return create_user(user, db)


# Login
@app.post("/login", tags=["login"])
def login(user: UserLogin = Depends(security), db: Session = Depends(get_db)):
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
    return authenticate_user(user, db)


# Create a new employee
@app.post("/employee", dependencies=[Depends(login)], tags=["employee"], response_model=EmployeeRead)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
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
    return add_employee(employee, db)

# List all employees
@app.get("/employee", dependencies=[Depends(login)], tags=["employee"], response_model=List[EmployeeRead])
def view_all_employees(db: Session = Depends(get_db)):
    """
    Retrieves all employees from the database.

    Input:
        db (Session): The database session.

    Returns:
        List[EmployeeRead]: A list of all employees.

    Raises: HTTPException: If there is a database error.
    """
    return get_all_employees(db)


# Search employees by key
@app.post("/employee/{key}/{value}", dependencies=[Depends(login)], tags=["employee"], response_model=List[EmployeeRead])
def search_employee(key:str, value: str, db: Session = Depends(get_db)):
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
    search_request = SearchRequest(key=key, value=value)
    return search_employees(search_request, db)


# Update employee based on employee_id
@app.put("/employee/{employee_id}", dependencies=[Depends(login)], tags=["employee"], response_model=EmployeeRead)
def update_employee_endpoint(employee_id: int, employee: EmployeeCreate, db: Session = Depends(get_db)):
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
    return update_employee(employee_id, employee, db)


# upload employees from CSV to store in database
@app.post("/employee/upload", dependencies=[Depends(login)], tags=["upload/export employee"], response_model=List[EmployeeRead])
def bulk_upload_employees(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """
    Creates employees from a CSV file.
    
    Input:
        file (UploadFile): The CSV file containing employee data.
        db (Session): The database session.

    Returns:
        List[EmployeeRead]: A list of created employees.
        Raises: HTTPException: If there is an error processing the CSV file.
    """
    content = file.file.read().decode("utf-8").splitlines()
    csv_reader = csv.DictReader(content)
    return bulk_create_employees_from_csv(csv_reader, db)


# Export employees to CSV
@app.get("/employee/export_csv", dependencies=[Depends(login)], tags=["upload/export employee"])
def export_employees_csv(db: Session = Depends(get_db)):
    """
    Exports all employees to a CSV file.

    Input:
        db (Session): The database session.

    Returns:
        str: The CSV content as a string.

    Raises:
        HTTPException: If there are no employees found or if there is a database error.
    """
    csv_data = export_employees_to_csv(db)
    headers = {
        "Content-Disposition": 'attachment; filename="employees.csv"',
        "Content-Type": "text/csv",
    }
    return Response(csv_data, headers=headers)
