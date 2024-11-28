from final_evaluation.logic import authenticate_user, create_user, add_employee, get_all_employees, search_employees, update_employee, bulk_create_employees_from_csv, export_employees_to_csv
from final_evaluation.schemas import UserLogin, EmployeeCreate, SearchRequest
from final_evaluation.models import Base
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create an in-memory SQLite database
DATABASE_URL = "sqlite:///final_evaluation/test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    db = next(get_db())

    # Test create_user
    # user = UserLogin(user_id=90, password="password")
    # print("Create User:", create_user(user, db))

    user = HTTPBasicCredentials(username="90", password="password")
    # Test authenticate_user
    print("Authenticate User:", authenticate_user(user, db))

    # Test add_employee
    employee = EmployeeCreate(
        firstname="John",
        lastname="Doe",
        date_of_birth="1990-01-01",
        date_of_joining="2020-01-01",
        grade="A"
    )
    added_employee = add_employee(employee, db)
    print("Add Employee:", str(added_employee))

    # Test get_all_employees
    all_employees = get_all_employees(db)
    print("All Employees:")
    for emp in all_employees:
        print(str(emp))

    # Test search_employees
    search_request = SearchRequest(key="firstname", value="John")
    search_result = search_employees(search_request, db)
    print("Search Employees:")
    for emp in search_result:
        print(str(emp))

    # Test update_employee
    updated_employee = EmployeeCreate(
        firstname="Jane",
        lastname="Doe",
        date_of_birth="1991-02-02",
        date_of_joining="2021-02-02",
        grade="M3"
    )
    updated_emp = update_employee(added_employee.employee_id, updated_employee, db)
    print("Update Employee:", str(updated_emp))
