from sqlalchemy import Column, Integer, String
from config import Base

class Employee(Base):
    __tablename__ = 'employee'

    emp_no = Column(Integer, primary_key=True, index=True)
    emp_name = Column(String, index=True)
    location = Column(String, index=True)
    dept_id = Column(Integer)

    def __str__(self):
        return f"emp_no: {self.emp_no}, emp_name: {self.emp_name}, location: {self.location}, dept_id: {self.dept_id}"
