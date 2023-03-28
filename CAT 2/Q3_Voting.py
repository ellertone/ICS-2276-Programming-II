class Voter:
    def __init__(self, voter_card_id, national_id, first_name, middle_name, last_name, polling_station, date_of_birth, gender):
        self.voter_card_id = voter_card_id
        self.national_id = national_id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.polling_station = polling_station
        self.date_of_birth = date_of_birth
        self.gender = gender
    
    def display_voter_details(self):
        print("Voter Card ID: ", self.voter_card_id)
        print("National ID: ", self.national_id)
        print("First Name: ", self.first_name)
        print("Middle Name: ", self.middle_name)
        print("Last Name: ", self.last_name)
        print("Polling Station: ", self.polling_station)
        print("Date of Birth: ", self.date_of_birth)
        print("Gender: ", self.gender)
        
voter_list = []
# Interactive driver program
while True:
    print("\nWelcome to The Interim Independent Electoral Commission (IIEC)")
    print("Electronic Voting Management System (EVMS)")
    print("\nSelect an option:")
    print("1. Add new voter details")
    print("2. Display voter details")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("\nEnter the following voter details:")
        voter_card_id = input("Voter Card ID: ")
        national_id = input("National ID: ")
        first_name = input("First Name: ")
        middle_name = input("Middle Name: ")
        last_name = input("Last Name: ")
        polling_station = input("Polling Station: ")
        import re
        date_of_birth = input("Date of Birth (dd-mm-yyyy): ")
        while not re.match(r'\d{2}-\d{2}-\d{4}', date_of_birth):
            date_of_birth = input("Invalid format. Please enter your Date of Birth in the format dd-mm-yyyy: ")
        gender = input("Gender: ")
        
        voter = Voter(voter_card_id, national_id, first_name, middle_name, last_name, polling_station, date_of_birth, gender)
        voter_list.append(voter)
        print("\nVoter details added successfully.")
    
    elif choice == '2':
        if voter_list: # check if list is not empty
            # display voter details of all voters in list
            for voter in voter_list:
                print("\nVoter details")
                print("===================")
                voter.display_voter_details()
        else:
            print("\nNo voter details found. Please add voter details first.")
            
    elif choice == '3':
        print("\nExiting the program...")
        break
    
    else:
        print("\nInvalid choice. Please select a valid option.")

