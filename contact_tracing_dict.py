# Write a python program for contact tracing:

# - Display a menu of options
# 	Menu:
# 		 1 -> Add an item
# 		 2 -> Search
# 		 3 -> Exit (y/n)
# - Allow user to select item in the menu (check if valid)
# - Perform the selected option
# 		- Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
# 				   Use dictionary to store the info
# 				   Use the full name as key
# 				   The value is another dictionary of personal information
# 		- Option 2: Search, ask full name then display the record
# 		- Option 3: Ask the user if want to exit or retry.

# Note: 
# - Your program should be uploaded to github before 4pm
# - Record a demo presenting your program
# - Send the demo or link of demo directly to my messenger

# Example Output:

# Menu:
#  1 -> Add an item
#  2 -> Search
#  3 -> Exit (y/n)

# What do you want to do? (1-3): 1
# Full name: Danilo Madrigalejos
# Age: 30
# Address: Eastwood
# Phone number: 1234567890
# Saved!
# What do you want to do? (1-3): 2
# Full name: Danilo Madrigalejos
# Age: 30
# Address: Eastwood
# Phone number: 1234567890 What do you want to do? (1-3): 3
# Exit? n

#while loop

while True: 

    #display menu
    print("*************** This is a Contact Tracing ****************")
    print()
    print("Press 1 -> Add an item/s")
    print("Press 2 -> Search existing item/s")
    print("Press 3 -> Exit the program")
    print()
    print("*"*58)

    #user input
    option = int(input("What do you want to do? (1-3): "))

    #dictionary
    contact = {}

    #diplay first option (add an item/s)
    if option == 1:

        print("You chose item 1, please state the required information.") 
        name = input("Enter your full name: ")
        age = int(input("Enter your age: "))
        address = input("Enter your address: ")
        contact_num = int(input("Enter your contact number: "))
        gender = input("State your gender. Put N/A if you prefer not to say: ")
        course = input("State your course in college: ")
        student_num = input("Enter your student number. Put N/A if not applicable: ")
        print("Your data have been saved!")
