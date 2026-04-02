'''
# Employee Management System (Intermediate)

i) This task will help you practice:
- lists
- dictionaries
- functions
- loops
- conditions
- CRUD operations
- search & update logic


ii) Problem Statement
Create a menu-driven Employee Management System.
The program should allow users to:

- Add employee
- View all employees
- Search employee by ID
- Update salary
- Delete employee
- Find highest salary employee
- Exit
- Requirements

iii) Each employee should have:
- id
- name
- department
- salary

Store data in a list of dictionaries
'''

employees = []

def add_employee():
    emp_id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "salary": salary
    }

    employees.append(employee)
    print("Employee added successfully")


def view_employees():
    if not employees:
        print("No employees found")
        return

    for emp in employees:
        print(emp)


def search_employee():
    emp_id = int(input("Enter employee ID to search: "))

    for emp in employees:
        if emp["id"] == emp_id:
            print(emp)
            return

    print("Employee not found")


def update_salary():
    emp_id = int(input("Enter employee ID: "))

    for emp in employees:
        if emp["id"] == emp_id:
            new_salary = float(input("Enter new salary: "))
            emp["salary"] = new_salary
            print("Salary updated successfully")
            return

    print("Employee not found")


def delete_employee():
    emp_id = int(input("Enter employee ID: "))

    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            print("Employee deleted successfully")
            return

    print("Employee not found")


def highest_salary():
    if not employees:
        print("No employees found")
        return

    highest = max(employees, key=lambda x: x["salary"])
    print("Highest Salary Employee:")
    print(highest)


while True:
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Delete Employee")
    print("6. Highest Salary Employee")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        update_salary()
    elif choice == "5":
        delete_employee()
    elif choice == "6":
        highest_salary()
    elif choice == "7":
        print("Exiting...")
        break
    else:
        print("Invalid choice")