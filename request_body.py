from fastapi import FastAPI
from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    department: str
    number: str
    employee_type: str | None = "full_time"
    

app=FastAPI()

@app.post("/employee/")
def create_employee(employee: Employee):
    employee.name=employee.name.capitalize()
    if len(employee.number) != 10:
        return {"error": "Number should be exactly 10 digits"}
    if not employee.number.isdigit():
        return {"error":"Number should only contain digits"}
    return employee