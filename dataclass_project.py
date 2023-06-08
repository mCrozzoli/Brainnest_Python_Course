'''
Task Overview: Employee Management System using Dataclasses

Build a Python program to manage employee records using dataclasses. Implement the following tasks:

    Define an Employee class using dataclasses with attributes like name, age, department, and salary.

    Create an empty list to store employee objects.

    Add employees to the system by creating instances of the Employee class and adding them to the list.

    Display the details of all employees in the system.

    Allow for updating employee details, such as salary, by searching for an employee by name.

    Provide the functionality to remove an employee from the system by searching for them by name.

    Display the updated details of the remaining employees.

Note: You can expand the project by adding search or sorting functionality, or by storing the employee data in a database or file.
'''

from dataclasses import dataclass
from typing import List

@dataclass
class Employee:
    name: str
    age: int
    department: str
    salary: float

# Use a dictionary to store employees using name as the key
employees = {}

class EmployeeManager:

    @classmethod
    def add_employee(cls, name, age, department, salary):
        employee = Employee(name, age, department, salary)
        employees[name] = employee

    @classmethod
    def display_employees(cls):
        for employee in employees.values():
            print(employee)

    @classmethod
    def update_employee(cls, name, salary):
        if name in employees:
            employees[name].salary = salary
            print(f"Salary of {name} updated successfully!")
        else:
            print("Employee not found!")

    @classmethod
    def remove_employee(cls, name):
        if name in employees:
            del employees[name]
            print(f"Employee {name} removed successfully!")
        else:
            print("Employee not found!")

# Adding employees to the system
EmployeeManager.add_employee("John", 28, "Sales", 50000)
EmployeeManager.add_employee("Emily", 32, "HR", 60000)
EmployeeManager.add_employee("Alex", 25, "Marketing", 45000)

# Displaying employee details
print("\nEmployees before updating and removing:")
EmployeeManager.display_employees()

# Updating salary of an employee
EmployeeManager.update_employee("John", 55000)

# Removing an employee
EmployeeManager.remove_employee("Emily")

# Displaying employee details after updating and removing
print("\nEmployees after updating and removing:")
EmployeeManager.display_employees()


'''
Employee is a simple class that stores data about an employee. It uses the @dataclass decorator, which is a feature of Python 3.7 and newer. This decorator automatically adds special methods to the class, such as __init__ and __repr__, that are needed for initializing and representing the class objects in a proper way.

The Employee class has four fields: name, age, department, and salary, with their types being defined after the colon.


The EmployeeManager class is a utility class that handles all operations related to employees. This class contains class methods for adding, displaying, updating, and removing employees. Class methods are methods that are bound to the class and not the instance of the class. They can modify a class state that would apply across all instances of the class, but not to any specific instance of the class.

add_employee method: This method creates a new Employee object and stores it in the employees dictionary. The employee's name is used as the key.

display_employees method: This method prints all Employee objects stored in the employees dictionary.

update_employee method: This method updates the salary of a specific Employee object. If the employee is not found in the dictionary, it prints a message saying "Employee not found!".

remove_employee method: This method removes a specific Employee object from the employees dictionary. If the employee is not found, it prints a message saying "Employee not found!".

Finally, the script at the bottom is using these class methods to add, display, update, and remove employees, and to display the results of these operations.
'''