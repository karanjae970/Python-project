print(" WELCOME TO SOCIETIES REGISTRATION SYSTEM ")

def chemistry_society():
    details = {}
    details["Name"] = input("Enter your name: ")
    details["Registration Number"] = input("Enter your registration number: ")
    print("You have registered for the ChemistSociety.")
    print("Your details are:")
    for key, value in details.items():
        print(f"{key}: {value}")
    print(f"Thank you {details['Name']} for registering!")
    return details
def informatics_society():
    details = {}
    details["Name"] = input("Enter your name: ")
    details["Registration Number"] = input("Enter your registration number: ")
    print("You have registered for the Informatics Society.")
    print("Your details are:")
    for key, value in details.items():
        print(f"{key}: {value}")
    print(f"Thank you {details['Name']} for registering!")
    return details
def physics_society():
    details = {}
    details["Name"] = input("Enter your name: ")
    details["Registration Number"] = input("Enter your registration number: ")
    print("You have registered for the Physics Society.")
    print("Your details are:")
    for key, value in details.items():
        print(f"{key}: {value}")
    print(f"Thank you {details['Name']} for registering!")
    return details
def mathematics_society():
    details = {}
    details["Name"] = input("Enter your name: ")
    details["Registration Number"] = input("Enter your registration number: ")
    print("You have registered for the Mathematics Society.")
    print("Your details are:")
    for key, value in details.items():
        print(f"{key}: {value}")
    print(f"Thank you {details['Name']} for registering!")
    return details
def kiswahili_society():
    details = {}
    details["Name"] = input("Enter your name: ")
    details["Registration Number"] = input("Enter your registration number: ")
    print("You have registered for the Kiswahili Society.")
    print("Your details are:")
    for key, value in details.items():
        print(f"{key}: {value}")
    print(f"Thank you {details['Name']} for registering!")
    return details


while True:
    print("1. Chemistry Society\n2. Informatics Society\n3. Physics Society\n4. Mathematics Society\n5. Kiswahili Society\n6. Exit")
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            chemistry_society()
        case 2:
            informatics_society()
        case 3:
            physics_society()
        case 4:
            mathematics_society()
        case 5:
            kiswahili_society()
        case 6:
            view_registered_members()
        case 7:
            print("Thank you for using the Societies Registration System.")
            break
        case _:
            print("Invalid choice. Please try again.")
            choice = int(input("Enter your choice: "))