# define a class for Voter with attributes and methods
import uuid
import re

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
        # display the details of a voter
        print("Voter Card ID: ", self.voter_card_id)
        print("National ID: ", self.national_id)
        print("First Name: ", self.first_name)
        print("Middle Name: ", self.middle_name)
        print("Last Name: ", self.last_name)
        print("Polling Station: ", self.polling_station)
        print("Date of Birth: ", self.date_of_birth)
        print("Gender: ", self.gender)

# create an empty list to store the voters
voter_list = []
test = Voter("00001", "1000", "Uhuru", "Mwigai", "Kenyatta", "Gatundu", "12-12-1963", "Male")
voter_list.append(test)

# Interactive driver program
while True:
    # display menu
    print("\nWelcome to The Interim Independent Electoral Commission (IIEC)")
    print("Electronic Voting Management System (EVMS)")
    print("\nSelect an option:")
    print("1. Add new voter details")
    print("2. Display voter details")
    print("3. Delete voter details")
    print("4. Exit")
    choice = input("Enter your choice: ")
    

    # add new voter details
    if choice == '1':
        print("\nEnter the following voter details:")
        voter_card_id = str(uuid.uuid4())[:5]
        national_id = input("National ID: ")
        first_name = input("First Name: ")
        middle_name = input("Middle Name: ")
        last_name = input("Last Name: ")
        polling_station = input("Polling Station: ")
        date_of_birth = input("Date of Birth (dd-mm-yyyy): ")
        # check for valid date format
        while not re.match(r'\d{2}-\d{2}-\d{4}', date_of_birth):
            date_of_birth = input("Invalid format. Please enter your Date of Birth in the format dd-mm-yyyy: ")
        gender = input("Gender: ")
        
        # create a new Voter object and append to the list
        voter = Voter(voter_card_id, national_id, first_name, middle_name, last_name, polling_station, date_of_birth, gender)
        voter_list.append(voter)
        print("\nVoter details added successfully.")
    
    # display voter details
    elif choice == '2':
        if voter_list: # check if list is not empty
            # display voter details of all voters in list
            for voter in voter_list:
                print("\nVoter details")
                print("===================")
                voter.display_voter_details()
        else:
            print("\nNo voter details found. Please add voter details first.")
   
   #delete voter details
    elif choice == '3':
        if voter_list: # check if list is not empty
            voter_card_id = input("\nEnter the Voter Card ID of the voter whose details you want to delete: ")
            for voter in voter_list:
                if voter.voter_card_id == voter_card_id:
                    voter_list.remove(voter)
                    print("\nVoter details deleted successfully.")
                    break
            else:
                print("\nVoter with Voter Card ID '{}' not found.".format(voter_card_id))
        else:
            print("\nNo voter details found. Please add voter details first.")
            
    # exit the program
    elif choice == '4':
        print("\nExiting the program...")
        break
    
    # invalid choice
    else:
        print("\nInvalid choice. Please select a valid option.")

