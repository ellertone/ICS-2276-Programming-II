class Employee:
    def __init__(self, emp_id, first_name, second_name, surname, gender, date_of_birth, basic_salary):
        self.emp_id = emp_id
        self.first_name = first_name
        self.second_name = second_name
        self.surname = surname
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.basic_salary = basic_salary

    def show_employee_details(self):
        print("\n\nEMPLOYEE DETAILS")
        print("================")
        print("Employee ID:", self.emp_id)
        print("Name:", self.first_name, self.second_name, self.surname)
        print("Gender:", self.gender)
        print("Date of Birth:", self.date_of_birth)
        print("Monthly Basic Salary:", self.basic_salary)

    def show_employee_pension(self):
        print("\nPENSIONS")
        print("===========")
        print("Employee ID:", self.emp_id)
        print("Name:", self.first_name, self.surname)
        print("Monthly Basic Salary:", self.basic_salary)
        print("Pension Contribution:", self.compute_pension())

    def compute_pension(self):
        return 0.05 * self.basic_salary


employee_list = []
emp_obj = Employee("78908", "MALCOM", "BUKE", "WAFULA", "M", "12-11-1984", 56789.45)
employee_list.append(emp_obj)

while True:
    print("\nEMPLOYEE MANAGEMENT SYSTEM")
    print("==========================")
    print("1. Add new employee details")
    print("2. Display employee details")
    print("3. Display employee pensions")
    print("4. Delete employee details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("\nEnter the following employee details:")
        emp_id = input("Employee ID: ")
        first_name = input("First Name: ")
        second_name = input("Second Name: ")
        surname = input("Last Name: ")
        gender = input("Gender: ")
        date_of_birth = input("Date of Birth (dd-mm-yyyy): ")
        basic_salary = float(input("Monthly Basic Salary: "))

        employee = Employee(emp_id, first_name, second_name, surname, gender, date_of_birth, basic_salary)
        employee_list.append(employee)
        print("\nEmployee details added successfully.")

    elif choice == '2':
        if employee_list:
            for employee in employee_list:
                employee.show_employee_details()
        else:
            print("\nNo employee details found. Please add employee details first.")

    elif choice == '3':
        if employee_list:
            print("EMPLOYEE DETAILS")
            print("================")
            for employee in employee_list:
                employee.show_employee_pension()
        else:
            print("\nNo employee details found. Please add employee details first.")

    elif choice == '4':
        emp_id = input("Enter the ID of the employee you want to delete: ")
        for employee in employee_list:
                if employee.emp_id == emp_id:
                    employee_list.remove(employee)
                    print("\nEmployee record deleted successfully.")
                    break
                else:
                    print("\nEmployee record not found.")

    elif choice == '5':
        print("\nExiting the program...")
        break

    else:
        print("\nInvalid choice. Please select a valid option.")
