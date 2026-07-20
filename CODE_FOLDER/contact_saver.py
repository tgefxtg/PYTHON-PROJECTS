# THIS IS LIBRARY :

    #-> GIVING TEXT CENTER - SHUTIL
from rich.console import Console

console = Console()

# HEADLINE OF CONTACT SAVER
console.print("+---------------+", justify="center")
console.print("[bold cyan]| CONTACT SAVER |[/bold cyan]", justify="center")
console.print("+---------------+", justify="center")

#EMPTY SET
contacts = {}

#LOOP
while True:
    print()
    # GIVING OPTIONS
    print("+-------------------------+")
    print("|1|      ADD  CONTACT     |")
    print("|2| VIEW  SAVED  CONTACTS |")
    print("|3|          EXIT         |")
    print("+-------------------------+")

    # ASKING USER THE CHOICE
    print()
    print()
    choice = input("ENTER YOUR OPTION: ")

    #USING IF ELSE CONDITION
        # ON CHOICE ONE ADDING THW USER DETAILS
    if choice == "1":
        print()
        print("+--------------------------+".center(shutil.get_terminal_size().columns))
        print("|ENTER YOUR CONTACT DEATILS|".center(shutil.get_terminal_size().columns))
        print("+--------------------------+".center(shutil.get_terminal_size().columns))
        print()
        name = input("ENTER YOUR NAME: ")
        number  = input("ENTER YOUR NUMBER: ")
        
        # SAVING THE PERSONS DETAILES
        contacts[name] = number

        # INFORMING THE USER THAT CONTACT HAS BEEN SAVED SUCCESSFULLY


        # ON CHOICE 2 VEIWIN THE SAVED CONTACTS
    elif choice == "2":
        if len(contacts) == 0:
            print()
            print("+------------------+")
            print("| NO CONTACT SAVED |")
            print("+------------------+")
        else:

            # LETTING USER KNOW THAT SAVED CONTACTS AS HEADINGN 
            print("+----------------+".center(shutil.get_terminal_size().columns))
            print("| SAVED CONTACTS |".center(shutil.get_terminal_size().columns))
            print("+----------------+".center(shutil.get_terminal_size().columns))
        
            # PRINTING THE SAVED CONTACTS
            for name in contacts:
                print("NAME: ",name)
                print("PHONE NUMBER: ",contacts[name])
        
            # PRINTING OR INFORMING THE USER THAT FINISHED
            print("+------------+".center(shutil.get_terminal_size().columns))
            print("|  FINISHED  |".center(shutil.get_terminal_size().columns))
            print("+------------+".center(shutil.get_terminal_size().columns))

    elif choice == "3":
        print()
        print("+----------------------------+".center(shutil.get_terminal_size().columns))
        print("| THANKYOU FOR USING OUR APP |".center(shutil.get_terminal_size().columns))
        print("+----------------------------+".center(shutil.get_terminal_size().columns))
        break

    else:
        print("| INVALID INPUT |")