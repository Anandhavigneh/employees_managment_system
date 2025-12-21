# Employee Management System
## Project Overview

The Employee Management System is a Python-based command-line application that helps manage employee records efficiently.
It allows users to add, view, update, delete, save, and load employee details using a menu-driven interface.

This project is designed for learning core Python concepts such as dictionaries, functions, file handling, and exception handling.

Features
Add employee details
View all employees
Update existing employee information
Delete employee records
Save employee data to a file
Load employee data from a file
Menu-driven command line interface
Error handling for safe execution
Technologies Used
Python 3
Command Line Interface (CLI)
File Handling
Dictionaries
Exception Handling
Project Structure
employee-management-system/
│
├── employee.py
└── README.md

Application Flow
Program starts with a main menu
User selects an option from the menu
Corresponding function is executed
Employee data is stored using a dictionary
Data can be saved to or loaded from a file
Program runs until the user chooses exit
Employee Data Format
{
  "101": {
    "name": "Anand",
    "age": "25",
    "salary": "40000",
    "department": "IT"
  }
}

Menu Options
1. Add Employee
2. View Employee
3. Update Employee
4. Delete Employee
5. Save to File
6. Load from File
7. Exit

Core Functions
Add Employee

Adds a new employee record using employee ID as the key.

add_empolyee(emp_id, name, age, salary, department)

View Employee

Displays all employee records stored in memory.

view_employee()

Update Employee

Updates one or more details of an existing employee.

update_employee(emp_id, name=None, age=None, salary=None, department=None)

Delete Employee

Removes an employee record using employee ID.

remove_employee(emp_id)

Save to File

Saves employee data into a file.

save_to_file(filename)

Load from File

Loads employee data from a file back into memory.

load_from_file(filename)

How to Run the Project
Step 1

Make sure Python 3 is installed on your system.

Step 2

Clone or download this repository.

Step 3

Open terminal or command prompt in the project folder.

Step 4

Run the application.

python employee.py

Sample Output
Welcome to the employee management system
1. Add employee
2. View employee
3. Update employee
4. Delete employee
5. Save to file
6. Load from file
7. Exit

Error Handling
Handles invalid employee IDs
Handles missing files
Prevents application crashes using try-except blocks
Future Enhancements
Use JSON file instead of text file
Add input validation
Convert age and salary to numeric values
Add search functionality
Build GUI or web-based version
Learning Outcomes
Understand CRUD operations
Learn dictionary-based data storage
Practice file handling in Python
Build menu-driven applications
Improve problem-solving skills
Disclaimer

This project is created for educational and learning purposes only.
It is not intended for production use.
