from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from logic import Logic

app = FastAPI()
l1 = Logic()

class Employee(BaseModel):
    emp_no: int
    emp_name: str
    location: str
    dept_id: int

@app.get("/get_employees", status_code=status.HTTP_200_OK)
def get_employee():
    result = l1.get_employees()
    if len(result) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "No employee found."
        )
    return result

@app.put("/update_employees", status_code=status.HTTP_200_OK)
def update_employee(update_employee: Employee):
    result = l1.update_employee(update_employee)
    if result is False:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail= f"Employee with emp_no {update_employee.emp_no} not found."
        )
    return result

@app.get("/get_employee_by_emp_no", status_code=status.HTTP_200_OK)
def get_employee_by_emp_no(emp_no: int):
    result = l1.get_employee_by_emp_no(emp_no)
    if result is False:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= f"Employee not found with emp_no {emp_no}"
        )
    return result

@app.get("/get_employee_by_location", status_code=status.HTTP_200_OK)
def get_employee_by_location(location: str):
    result = l1.get_employee_by_location(location)
    if len(result) == 0: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= f"No employee found from location {location}."
        )
    return result
