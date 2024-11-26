from datetime import date
from typing import Optional

from pydantic import BaseModel


class UserLogin(BaseModel):
    """
    Schema for user login details.
    """
    user_id: int
    password: str

class UserRead(UserLogin):
    """
    Schema for reading user details.
    
    Inherits all attributes from UserLogin.
    """
    class Config:
        """
        Config: 
            orm_mode (bool): Enables compatibility with ORM (Object Relational Mapper) for reading data.
        """
        from_attributes = True

class EmployeeCreate(BaseModel):
    """
    Schema for creating a new employee.
    
    All attributes are optional to partially updates the field we want to update.
    """
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    date_of_birth: Optional[date] = None
    date_of_joining: Optional[date] = None
    grade: Optional[str] = None

class EmployeeRead(EmployeeCreate):
    """
    Schema for reading employee details.
    
    Inherits all attributes from EmployeeCreate.
    """
    employee_id: int
    class Config:
        """
        Config: 
            orm_mode (bool): Enables compatibility with ORM (Object Relational Mapper) for reading data.
        """
        from_attributes = True

class SearchRequest(BaseModel):
    """
    Schema for search requests.
    """
    key: str
    value: str
