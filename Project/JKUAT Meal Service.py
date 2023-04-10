#import the json library
import json

class User:
    def __init__(self, username, password):
        # Initialize a User object with a username and password
        self.username = username
        self.password = password


class MealTicket:
    def __init__(self, meal_code, meal_name, meal_price, quantity):
        # Initialize a MealTicket object with a meal code, meal name, meal price, and quantity
        self.meal_code = meal_code
        self.meal_name = meal_name
        self.meal_price = meal_price
        self.quantity = quantity
        self.total_cost = meal_price * quantity


class Student(User):
    def __init__(self, username, password, student_id, balance):
        # Initialize a Student object with a username, password, student ID, balance, and an empty list of meal tickets
        super().__init__(username, password)
        self.student_id = student_id
        self.meal_tickets = []
        self.balance = balance
        self.sales = Sales()

    def place_order(self, meal_code, quantity):
        # Allow the student to place an order by creating a MealTicket object, adding it to the student's list of meal tickets,
        # and recording the sale in the system's Sales object
        if meal_code not in MEAL_OPTIONS:
            print("Invalid meal code, please try again")
            return

        meal_name, meal_price = MEAL_OPTIONS[meal_code]
        meal_ticket = MealTicket(meal_code, meal_name, meal_price, quantity)
        self.meal_tickets.append(meal_ticket)

        self.balance -= meal_ticket.total_cost
        self.sales.record_sale(self.student_id, meal_ticket)


    def cancel_order(self, meal_ticket):
        # Allow the student to cancel an order by removing the corresponding MealTicket object from their list of meal tickets
        # and adding the cost back to their balance
        self.meal_tickets.remove(meal_ticket)

        self.balance += meal_ticket.total_cost


class Admin(User):
    def __init__(self, username, password, admin_id):
        # Initialize an Admin object with a username, password, and admin ID
        super().__init__(username, password)
        self.admin_id = admin_id

    def view_sales(self):
        # Display the total sales and a breakdown of sales by meal for all recorded sales in the system's Sales object
        with open('sales.json', "r") as f:
            sales_data = json.load(f)
            total_sales = sum(sale['total_cost'] for sale in sales_data)
            print(f"Total sales: {total_sales}")
            print("Sales breakdown by meal:")
            for meal_code in MEAL_OPTIONS.keys():
                meal_name, meal_price = MEAL_OPTIONS[meal_code]
                quantity_sold = sum(sale['quantity'] for sale in sales_data if sale['meal_code'] == meal_code)
                total_sales_for_meal = sum(sale['total_cost'] for sale in sales_data if sale['meal_code'] == meal_code)
                print(f"{meal_name}: {quantity_sold} sold for a total of {total_sales_for_meal}")

    def add_meal(self, meal_code, meal_name, meal_price):
        # Add a new meal option to the system's MEAL_OPTIONS dictionary
        MEAL_OPTIONS[meal_code] = (meal_name, meal_price)

    def remove_meal(self, meal_code):
        # Remove a meal option from the system's MEAL_OPTIONS dictionary
        if meal_code in MEAL_OPTIONS:
            del MEAL_OPTIONS[meal_code]

    def create_student_account(self):
        # Prompt the admin to create a new student account and add it to the system's STUDENTS dictionary and students.json file
        username = input("Enter a username for the student: ")
        password = input("Enter a password for the student: ")
        student_id = input("Enter a student ID: ")
        balance = int(input("Enter a starting balance: "))
        with open('students.json', 'r+') as f:
            students_data = json.load(f)
            students_data.append({'username': username, 'password': password, 'student_id': student_id, 'balance': balance})
            f.seek(0)
            json.dump(students_data, f, indent=4)

        if username in system.students:
            print("A user with that username already exists.")
        else:
            student = Student(username, password, student_id, balance)
            system.students[username] = student
            print(f"Student account created with username: {username}")

    def view_student_accounts(self):
        # Display a list of all the students in the system's STUDENTS dictionary
        for username, student in system.students.items():
            print(f"Username: {username}, Student ID: {student.student_id}, Balance: {student.balance}")

# Define a Sales class to manage the sales record
class Sales:
    # Initialize an empty sales record list
    def __init__(self):
        self.sales_record = []

    # Record a sale by adding the sale details to the sales record list and updating the sales data file
    def record_sale(self, student_id, meal_ticket):
        # Open the sales data file and load the existing sales data into a list
        with open('sales.json', 'r') as f:
            sales_data = json.load(f)

        # Create a new sales record dictionary with the provided sale details
        new_sale = {'student_id': student_id,
                    'meal_code': meal_ticket.meal_code,
                    'meal_name': meal_ticket.meal_name,
                    'meal_price': meal_ticket.meal_price,
                    'quantity': meal_ticket.quantity,
                    'total_cost': meal_ticket.total_cost}

        # Add the new sales record to the sales data list
        sales_data.append(new_sale)

        # Open the sales data file in write mode and update it with the updated sales data list
        with open('sales.json', 'w') as f:
            json.dump(sales_data, f, indent=4)


class System:
    def __init__(self):
        # Load students, admins and sales data from files
        self.students = self.load_students_from_file()
        self.admins = self.load_admins_from_file()
        self.sales = Sales()
        self.login_attempts = 0
        
    def load_admins_from_file(self):
        # Load data from admins file
        with open('admins.json', 'r') as f:
            admins_data = json.load(f)

        admins = {}
        # Create an Admin object for each admin data and add it to the dictionary
        for admin_data in admins_data:
            admin = Admin(admin_data['username'], admin_data['password'], admin_data['admin_id'])
            admins[admin_data['username']] = admin

        return admins


    def load_students_from_file(self):
        # Load data from students file
        with open('students.json', 'r') as f:
            students_data = json.load(f)

        students = {}
        # Create a Student object for each student data and add it to the dictionary
        for student_data in students_data:
            student = Student(student_data['username'], student_data['password'], student_data['student_id'], student_data['balance'])
            students[student_data['username']] = student

        return students

    def login(self):
        print("\nWELCOME TO THE JKUAT MEAL SERVICE.\n")
        print("Please enter your details to log in.")
    
        for attempt in range(3):
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if username in self.admins:
                if self.admins[username].password == password:
                    print("\nLogin successful as admin.")
                    return self.admins[username]
                else:
                    print("Incorrect password.")

            elif username in self.students:
                if self.students[username].password == password:
                    print("\nLogin successful as student.")
                    return self.students[username]
                else:
                    print("Incorrect password.")

            print(f"Invalid username or password. Attempts remaining: {2-attempt}")

        print("Maximum number of login attempts reached.")
        exit()


MEAL_OPTIONS = {
    "1": ("Tea", 15),
    "3": ("Bread Slice", 3),
    "7": ("Ndazi", 10),
    "9": ("Coffee", 15),
    "13": ("Chapati", 20),
    "14": ("Bun", 20),
    "15": ("Sukuma", 13),
    "16": ("Beef", 120),
    "17": ("Ugali", 15),
    "18": ("Bean", 20),
    "20": ("Rice", 23),
    "21": ("African Stew", 30),
    "22": ("Omelette", 20),
    "24": ("Githeri", 20),
    "47": ("Boiled Egg", 20)
}



 # Call the login method of the system object to authenticate the user
sales = Sales()
system = System()
user = system.login()


# Check if the user is a student
if isinstance(user, Student):
        # Display welcome message and current balance
        print(f"Welcome {user.username}. Your balance is {user.balance}.\n")
        # Loop until the user logs out
        while True:
            # Display options for the student
            print("Please select an option:")
            print("1. Place order")
            print("2. Cancel order")
            print("3. View order history")
            print("4. Logout")
            # Get user input for selected option
            option = input("\nEnter option number: ")
            # If option 1 is selected
            if option == "1":
                # Display available meals and their codes and prices
                print("\nHere are the available meals:\n")
                print("Code  |  Name  |  Price")
                for code, (name, price) in MEAL_OPTIONS.items():
                    print(f"{code}  |  {name}  |  {price}")
                # Get user input for meal code and quantity
                meal_code = input("\nEnter meal code: ")
                quantity = int(input("Enter quantity: "))
                meal_price = MEAL_OPTIONS[meal_code][1]
                total_cost = meal_price * quantity
                # Check if user has enough balance to place the order
                if user.balance >= total_cost:
                    # Place the order and display message with updated balance
                    user.place_order(meal_code, quantity)
                    print("Order placed successfully!Your balance is", user.balance)
                else:
                    # Display message if user has insufficient balance
                    print("Sorry, you do not have enough balance to place this order.Your balance is",user.balance)
            # If option 2 is selected
            elif option == "2":
                # Display current orders of the user
                print("Here are your current orders:\n")
                print("Code  |  Name  |  Price | Quantity | Total Cost")
                for meal_ticket in user.meal_tickets:
                    print(f"{meal_ticket.meal_code} | {meal_ticket.meal_name} | {meal_ticket.meal_price} | {meal_ticket.quantity} | {meal_ticket.total_cost}")
                # Get user input for the ticket code of the order to be cancelled
                ticket_code = input("\nEnter ticket code to cancel: ")
                # Loop through the user's meal tickets to find the order with the ticket code
                for meal_ticket in user.meal_tickets:
                    if meal_ticket.meal_code == ticket_code:
                        # Cancel the order and display success message
                        user.cancel_order(meal_ticket)
                        print("\nOrder cancelled successfully!\n")
                        break
                else:
                    # Display message if invalid ticket code is entered
                    print("Invalid ticket code, please try again")
            # If option 3 is selected
            elif option == "3":
                # Display order history of the user
                print("Here are your order history:")
                print("Code  |  Name  |  Price | Quantity | Total Cost")
                for meal_ticket in user.meal_tickets:
                    print(f"{meal_ticket.meal_code} | {meal_ticket.meal_name} | {meal_ticket.meal_price} | {meal_ticket.quantity} | {meal_ticket.total_cost}")

            elif option == "4":
                # Update student's balance in students.json before logging out
                with open('students.json', 'r') as f:
                    students = json.load(f)

                for student in students:
                    if student['username'] == user.username:
                        student['balance'] = user.balance
                        break

                with open('students.json', 'w') as f:
                    json.dump(students, f, indent=4)
                print("Thank you for using JKUAT Meal Service!")
                break
            else:
                print("Invalid option, please try again.")

   # If the logged in user is an admin
elif isinstance(user, Admin):
        # Print a welcome message for the admin
    print(f"Welcome {user.username}.\n")
        
        # Keep looping until the admin logs out
    while True:
            # Display the available options for the admin
            print("\n Please select an option:")
            print("1. View sales")
            print("2. Add meal")
            print("3. Remove meal")
            print("4. Create student account")
            print("5. View student accounts")
            print("6. Logout \n")

            # Get the admin's option choice
            option = input("Enter option number: ")
            
            # If option 1 is selected
            if option == "1":
                # View the total sales made by the system
                sales = user.view_sales()

            # If option 2 is selected
            elif option == "2":
                # Add a new meal to the available options
                meal_code = input("Enter meal code: ")
                meal_name = input("Enter meal name: ")
                meal_price = int(input("Enter meal price: "))
                user.add_meal(meal_code, meal_name, meal_price)
                print("Meal added successfully!")
                
            # If option 3 is selected
            elif option == "3":
                # Remove a meal from the available options
                meal_code = input("Enter meal code to remove: ")
                user.remove_meal(meal_code)
                print("Meal removed successfully!")
                
            # If option 4 is selected
            elif option == "4":
                # Create a new student account
                user.create_student_account()
                
            # If option 5 is selected
            elif option == "5":
                # Display all existing student accounts
                user.view_student_accounts()
                
            # If option 6 is selected
            elif option == "6":
                # Print a logout message for the admin
                print("Thank you for using JKUAT Meal Service!")
                break
                
            # If an invalid option is selected
            else:
                print("Invalid option, please try again")
else: 
    print("User not found, exiting system")
    exit()
