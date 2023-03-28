class Person:
    def __init__(self, age, firstname, lastname):
        self.age = age
        self.firstname = firstname
        self.lastname = lastname

    def getValues(self):
        print("Name:", self.firstname, self.lastname)
        print("Age:", self.age)

    def setValues(self, age, firstname, lastname):
        self.age = age
        self.firstname = firstname
        self.lastname = lastname


class Student(Person):
    def __init__(self, age, firstname, lastname, institution, year, reg_number):
        super().__init__(age, firstname, lastname)
        self.institution = institution
        self.year = year
        self.reg_number = reg_number

    def getValues(self):
        super().getValues()
        print("Institution:", self.institution)
        print("Year:", self.year)
        print("Registration Number:", self.reg_number)

    def setValues(self, age, firstname, lastname, institution, year, reg_number):
        super().setValues(age, firstname, lastname)
        self.institution = institution
        self.year = year
        self.reg_number = reg_number


s = Student(20, "Alice", "Smith", "ABC University", 2, "12345")
s.getValues()
s.setValues(21, "Bob", "Johnson", "DEF University", 3, "67890")
s.getValues()




