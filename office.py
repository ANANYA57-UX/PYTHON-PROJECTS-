

# Temporary data storage
employees = []
attendance = []
tasks = []


def header():
    print("\n" + "=" * 50)
    print("OFFICE HUB")
    print("OFFICE MANAGEMENT SYSTEM")
    print("=" * 50)




def employee_management():

    while True:

        print("\n========== EMPLOYEE MANAGEMENT ==========")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Back to Main Menu")

        choice = input("\nEnter your choice: ").strip()

        # Add Employee
        if choice == "1":

            emp_id = input("Enter Employee ID: ").strip()

            found = False

            for emp in employees:
                if emp["id"] == emp_id:
                    found = True

            if found:
                print("Employee ID already exists!")
                continue

            name = input("Enter Name: ").strip()
            department = input("Enter Department: ").strip()

            try:
                salary = float(input("Enter Salary: "))

                if salary < 0:
                    print("Salary cannot be negative!")
                    continue

            except ValueError:
                print("Please enter a valid salary!")
                continue

            employee = {
                "id": emp_id,
                "name": name,
                "department": department,
                "salary": salary
            }

            employees.append(employee)

            print("\nEmployee added successfully!")

        # View Employees
        elif choice == "2":
            print("VIEW EMPLOYEES FUNCTION IS WORKING!")

            if len(employees) == 0:
                print("No employees found.")

            else:
                for emp in employees:

                    print("\nEmployee ID :", emp["id"])
                    print("Name        :", emp["name"])
                    print("Department  :", emp["department"])
                    print("Salary      : ₹", emp["salary"])
                    print("-" * 40)

        # Update Employee
        elif choice == "3":

            emp_id = input("Enter Employee ID to update: ").strip()

            found = False

            for emp in employees:

                if emp["id"] == emp_id:

                    emp["name"] = input("Enter New Name: ").strip()
                    emp["department"] = input("Enter New Department: ").strip()

                    try:
                        new_salary = float(input("Enter New Salary: "))

                        if new_salary < 0:
                            print("Salary cannot be negative!")
                            break

                        emp["salary"] = new_salary

                    except ValueError:
                        print("Invalid salary!")
                        break

                    print("Employee updated successfully!")
                    found = True
                    break

            if not found:
                print("Employee not found!")

        # Delete Employee
        elif choice == "4":

            emp_id = input("Enter Employee ID to delete: ").strip()

            for emp in employees:

                if emp["id"] == emp_id:

                    employees.remove(emp)
                    print("Employee deleted successfully!")
                    break

            else:
                print("Employee not found!")

        # Back to Main Menu
        elif choice == "5":
            break

        else:
            print("Invalid choice! Try again.")



def attendance_management():

    print("\n========== ATTENDANCE MANAGEMENT ==========")

    emp_id = input("Enter Employee ID: ").strip()

    for emp in employees:

        if emp["id"] == emp_id:

            status = input("Enter Present or Absent: ").strip().title()

            if status not in ["Present", "Absent"]:
                print("Invalid attendance status!")
                return

            record = {
                "id": emp_id,
                "name": emp["name"],
                "status": status
            }

            attendance.append(record)

            print("Attendance marked successfully!")
            return

    print("Employee not found!")



def task_management():

    while True:

        print("\n========== TASK MANAGEMENT ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Back to Main Menu")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            emp_id = input("Enter Employee ID: ").strip()

            employee = None

            for emp in employees:
                if emp["id"] == emp_id:
                    employee = emp
                    break

            if employee is None:
                print("Employee not found!")
                continue

            description = input("Enter Task Description: ").strip()

            task = {
                "id": len(tasks) + 1,
                "description": description,
                "employee": employee["name"],
                "status": "Pending"
            }

            tasks.append(task)

            print("Task assigned successfully!")

        elif choice == "2":

            print("\n========== TASK LIST ==========")

            if len(tasks) == 0:
                print("No tasks available.")

            else:
                for task in tasks:

                    print("\nTask ID     :", task["id"])
                    print("Description :", task["description"])
                    print("Employee    :", task["employee"])
                    print("Status      :", task["status"])
                    print("-" * 40)

        elif choice == "3":

            try:
                task_id = int(input("Enter Task ID: "))
            except ValueError:
                print("Enter a valid task ID!")
                continue

            found = False

            for task in tasks:

                if task["id"] == task_id:
                    task["status"] = "Completed"
                    print("Task completed successfully!")
                    found = True
                    break

            if not found:
                print("Task not found!")

        elif choice == "4":
            break

        else:
            print("Invalid choice!")




def salary_management():

    print("\n========== SALARY MANAGEMENT ==========")

    emp_id = input("Enter Employee ID: ").strip()

    for emp in employees:

        if emp["id"] == emp_id:

            print("\nEmployee Name  :", emp["name"])
            print("Monthly Salary : ₹", emp["salary"])
            print("Annual Salary  : ₹", emp["salary"] * 12)

            return

    print("Employee not found!")




def office_reports():

    print("\n========== OFFICE REPORTS ==========")

    total_employees = len(employees)
    total_attendance = len(attendance)
    total_tasks = len(tasks)

    completed = 0
    pending = 0

    for task in tasks:

        if task["status"] == "Completed":
            completed += 1
        else:
            pending += 1

    print("Total Employees    :", total_employees)
    print("Attendance Records :", total_attendance)
    print("Total Tasks        :", total_tasks)
    print("Completed Tasks    :", completed)
    print("Pending Tasks      :", pending)



def search_employee():

    print("\n========== SEARCH EMPLOYEE ==========")

    emp_id = input("Enter Employee ID: ").strip()

    for emp in employees:

        if emp["id"] == emp_id:

            print("\nEmployee Found!")
            print("Employee ID :", emp["id"])
            print("Name        :", emp["name"])
            print("Department  :", emp["department"])
            print("Salary      : ₹", emp["salary"])

            return

    print("Employee not found!")




def main_menu():

    while True:

        header()

        print("\n1. Employee Management")
        print("2. Attendance Management")
        print("3. Task Management")
        print("4. Salary Management")
        print("5. Office Reports")
        print("6. Search Employee")
        print("7. Exit")

        print("\n" + "-" * 50)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            employee_management()

        elif choice == "2":
            attendance_management()

        elif choice == "3":
            task_management()

        elif choice == "4":
            salary_management()

        elif choice == "5":
            office_reports()

        elif choice == "6":
            search_employee()

        elif choice == "7":

            print("\nThank you for using OFFICE HUB!")
            print("Have a great day!")
            break

        else:
            print("\nInvalid choice! Please enter 1 to 7.")

main_menu()
