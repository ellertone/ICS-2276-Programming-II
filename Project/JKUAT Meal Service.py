import json

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class MealTicket:
    def __init__(self, meal_code, meal_name, meal_price, quantity):
        self.meal_code = meal_code
        self.meal_name = meal_name
        self.meal_price = meal_price
        self.quantity = quantity
        self.total_cost = meal_price * quantity

class Student(User):
    def __init__(self, username, password, student_id, balance):
        super().__init__(username, password)
        self.student_id = student_id
        self.meal_tickets = []
        self.balance = balance
        self.sales = sales

    def place_order(self, meal_code, quantity):
        if meal_code not in MEAL_OPTIONS:
            print("Invalid meal code, please try again")
            return

        meal_name, meal_price = MEAL_OPTIONS[meal_code]
        meal_ticket = MealTicket(meal_code, meal_name, meal_price, quantity)
        self.meal_tickets.append(meal_ticket)

        self.balance -= meal_ticket.total_cost
        self.sales.record_sale(self.student_id, meal_ticket)


    def cancel_order(self, meal_ticket):
        self.meal_tickets.remove(meal_ticket)

        self.balance += meal_ticket.total_cost


class Admin(User):
    def __init__(self, username, password, admin_id):
        super().__init__(username, password)
        self.admin_id = admin_id


    def view_sales(self):
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
        MEAL_OPTIONS[meal_code] = (meal_name, meal_price)

    def remove_meal(self, meal_code):
        if meal_code in MEAL_OPTIONS:
            del MEAL_OPTIONS[meal_code]

    def create_student_account(self):
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
        for username, student in system.students.items():
            print(f"Username: {username}, Student ID: {student.student_id}, Balance: {student.balance}")

class Sales:
    def __init__(self):
        self.sales_record = []

    def record_sale(self, student_id, meal_ticket):
        with open('sales.json', 'r') as f:
            sales_data = json.load(f)

        new_sale = {'student_id': student_id,
                    'meal_code': meal_ticket.meal_code,
                    'meal_name': meal_ticket.meal_name,
                    'meal_price': meal_ticket.meal_price,
                    'quantity': meal_ticket.quantity,
                    'total_cost': meal_ticket.total_cost}

        sales_data.append(new_sale)

        with open('sales.json', 'w') as f:
            json.dump(sales_data, f, indent=4)


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


class System:
    def __init__(self):
        self.students = self.load_students_from_file()
        self.admins = self.load_admins_from_file()
        self.sales = Sales()

    def load_admins_from_file(self):
        with open('admins.json', 'r') as f:
            admins_data = json.load(f)

        admins = {}
        for admin_data in admins_data:
            admin = Admin(admin_data['username'], admin_data['password'], admin_data['admin_id'])
            admins[admin_data['username']] = admin

        return admins


    def load_students_from_file(self):
        with open('students.json', 'r') as f:
            students_data = json.load(f)

        students = {}
        for student_data in students_data:
            student = Student(student_data['username'], student_data['password'], student_data['student_id'], student_data['balance'])
            students[student_data['username']] = student

        return students

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in self.students:
            if self.students[username].password == password:
                print("\nLogin successful as student.")
                return self.students[username]
            else:
                print("Incorrect password.")
        elif username in self.admins:
            if self.admins[username].password == password:
                print("\nLogin successful as admin.")
                return self.admins[username]
            else:
                print("Incorrect password.")
        else:
            print("User not found.")

print("\n Hello, welcome to JKUAT Meal Service.\n")
print("Please enter your details to log into the system: ")

sales = Sales()
system = System()
user = system.login()

if isinstance(user, Student):
    print(f"Welcome {user.username}. Your balance is {user.balance}.\n")
    while True:
        print("Please select an option:")
        print("1. Place order")
        print("2. Cancel order")
        print("3. View order history")
        print("4. Logout")

        option = input("\nEnter option number: ")
        if option == "1":
            print("\nHere are the available meals:\n")
            print("Code  |  Name  |  Price")
            for code, (name, price) in MEAL_OPTIONS.items():
                print(f"{code}  |  {name}  |  {price}")
            meal_code = input("\nEnter meal code: ")
            quantity = int(input("Enter quantity: "))
            meal_price = MEAL_OPTIONS[meal_code][1]
            total_cost = meal_price * quantity
            if user.balance >= total_cost:
                user.place_order(meal_code, quantity)
                print("Order placed successfully!Your balance is", user.balance)
            else:
                print("Sorry, you do not have enough balance to place this order.Your balance is",user.balance)

        elif option == "2":
            print("Here are your current orders:\n")
            print("Code  |  Name  |  Price | Quantity | Total Cost")
            for meal_ticket in user.meal_tickets:
                print(f"{meal_ticket.meal_code} | {meal_ticket.meal_name} | {meal_ticket.meal_price} | {meal_ticket.quantity} | {meal_ticket.total_cost}")
            ticket_code = input("\nEnter ticket code to cancel: ")
            for meal_ticket in user.meal_tickets:
                if meal_ticket.meal_code == ticket_code:
                    user.cancel_order(meal_ticket)
                    print("\nOrder cancelled successfully!\n")
                    break
            else:
                print("Invalid ticket code, please try again")
        elif option == "3":
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
elif isinstance(user, Admin):
    print(f"Welcome {user.username}.\n")
    while True:
        print("\n Please select an option:")
        print("1. View sales")
        print("2. Add meal")
        print("3. Remove meal")
        print("4. Create student account")
        print("5. View student accounts")
        print("6. Logout \n")

        option = input("Enter option number: ")
        if option == "1":
            sales = user.view_sales()

        elif option == "2":
            meal_code = input("Enter meal code: ")
            meal_name = input("Enter meal name: ")
            meal_price = int(input("Enter meal price: "))
            user.add_meal(meal_code, meal_name, meal_price)
            print("Meal added successfully!")
        elif option == "3":
            meal_code = input("Enter meal code to remove: ")
            user.remove_meal(meal_code)
            print("Meal removed successfully!")
        elif option == "4":
            user.create_student_account()
        elif option == "5":
            user.view_student_accounts()
        elif option == "6":
            print("Thank you for using JKUAT Meal Service!")
            break
        else:
            print("Invalid option, please try again")
else:
    print("Exiting system...")
input()
