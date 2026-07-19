# CONTACT SAVER 
# ------------- #

# EMPTY LIST

contacts = {}

# CONTACT SAVER ON "def"
def title():
    print("+================+")
    print("|  CONTACT SAVER |")
    print("+================+")

title()

# LOOP 
while True :
# OPTIONS

    print("+=====================+")
    print("|| 1 | ADD CONTACT   ||")
    print("+=====================+")
    print("|| 2 | VIEW CONTACT  ||")
    print("+=====================+")
    print("|| 3 | EXIT          ||")
    print("+=====================+")
    print()
    print()
# ASKING THE USER OPTIONS

    print("+----------------------+")
    choice = input("|ENTER YOUR OPTION:    |")
    print("+----------------------+")

    if choice == "1":
        name = input("ENTER NAME: ")
        number = input("ENTER NUMBER: ")

    # SAVING CONTACT
        contacts[name] = number

    # INFORMING THAT THE CONTACT HAS BEEN SAVED SUCCESSFULLY
        print("+----------------------------+")
        print("| CONTACT SAVED SUCCESSFULLY |")
        print("+----------------------------+")
        print()
        print()

    elif choice == "2":
        if len(contacts) == 0:
            print("---------------")
            print("| NO CONTACTS |")
            print("---------------")

        else:
            print()
            print("+-----------------+")
            print("SAVED CONTACT")
            print("+-----------------+")
            print()
            for name in contacts:
                print("NAME: ", name)
                print("CONTACT: ",contacts[name])
                print()
            print("+----------+")
            print("| FINISHED |")
            print("+----------+")

    elif choice == "3":
        
        print("THANK YOU")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN")
