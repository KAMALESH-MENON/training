from sqlalchemy import Column, Date, Integer, String

from .database import Base


class User(Base):
    """
    Model representing a user in the database.
    """
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, unique=True, index=True)
    password = Column(String)


class Employee(Base):
    """
    Model representing a employee in the database.
    """
    __tablename__ = "employees"

    employee_id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    date_of_birth = Column(Date)
    date_of_joining = Column(Date)
    grade = Column(String)
