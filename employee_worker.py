# employee worker 

# this is an empty set to store peoples information

employee = []
main_pass = 12345

# table
print("+------------------------------+")
print("| 1 | ADD DETAILS              |")
print("| 2 | VIEW WHOLE EMPLOYEE INFO |")
print("| 3 | VEIW NAME AND ID         |")
print("| 4 | CHANGE INFORMATION       |")
print("| 5 | CHANGE PERSONAL PASSWORD |")
print("+------------------------------+")
    
    #WHILE LOOP CONDITION
while True:
    try:
        choice = int(input("ENTER YOUR CHOICE: "))
    except ValueError:
        print("Please enter a number not Aphabets or Other")
        continue
    
    #IF CONDITION
    if choice == 1:

        # HEADING
        print("+-------------+")
        print("| ADD DETAILS |")
        print("+-------------+")
        print()

        # ASKING USER INFO
        name = input("ENTER YOUR NAME: ")
        age = int(input("ENTER YOUR AGE: "))
        birth = int(input("ENTER YOUR DATE OF BIRTH:"))
        department = input("WHICH DEPARTMENT YOU ARE: ")
        job = input("WHICH JOB YOU ARE WORKING ON: ")
        experience = int(input("YEAR OF EXPERIENCE YOU HAD: "))
        id = int(input("ENTER YOU ID: "))
        password = input("ENTER YOUR PASSWORD: ")
        print()

        #STORING DATAS
        employee.append({
                "Name": name,
                "Age" : age,
                "Birth":birth,
                "Department" : department,
                "Job" : job,
                "Experience" : experience,
                "Id" : id,
                "Password" : password 
                })
        print("YOUR DATA SAVED SUCCESSFULLY")

    elif choice == 2:

        # TABLE
        print("+--------------+")
        print("| VIEW DETAILS |")
        print("+--------------+")
        print()
        try:
            passcode = int(input("ENTER YOUR MAIN PASSCODE: "))
        except ValueError:
            print("Please enter Number not Alphabets or Others")
            continue
        print()

        if main_pass == passcode:
            for i in employee:
                print("Name: ", i["Name"])
                print("Age: ", i["Age"])
                print("Department: ", i["Department"])
                print("Job: ", i["Job"])
                print("Experience: ",i["Experience"])
                print("Id: ", i["Id"])
                print("Password: ",i["Password"])

        else:
            print("WRONG PASSCODE")

    elif choice == 3:

        #TABLE
        print("+------------------+")
        print("| VIEW NAME AND ID |")
        print("+------------------+")
        
        # ASKING PASSWORD
        name1 = input("ENTER YOUR NAME: ")

        pass_code = input("ENTER YOUR PASSWORD: ")
        print()

        # TABLE
        print("+---------------------+")
        print("| 0 | Forgot password |")
        print("+---------------------+")

        # IF ELSE CONDITION
        if pass_code == "0":
            
            #TABLE
            print()
            print()
            print("+------------------------+")
            print("| PASSWORD RECOVERY MODE |")
            print("+------------------------+")
            print()
            print()

            #ASKING USER AB0UT THE ID
            try:
                id1 = int(input("ENTER YOU ID: "))
            except ValueError:
                print("Please enter a Number not Alphabets or Other")
                continue

            found = False

            #LOOP CONDITION
            for i in employee:
                if i["Id"] == id1:
                    print()
                    print("+-----------------------+")
                    print("| HERE IS YOUR PASSWORD |")
                    print("+-----------------------+")
                    print()
                    print("Name: ",i["Name"])
                    print("Password: ", i["Password"])
                    found = True
                    break

                #IF ELSE CONDITION
            if found == False:
                print("WRONG ID, Please enter a Valid ID ")

        else:
            
            found = False

            #LOOP CONDITIOM
            for i in employee:
                if i["Name"].lower() == name1.lower() and i["Password"] == pass_code:

                    print()
                    print("Name: ", i["Name"])
                    print("ID: ", i["Id"])
                    found = True
                    break
                    
                    #IF CONDITION
                if found == False:
                    print("Invalid Password!")
                    print()

    #IF ELSE CONDITION
    elif choice == 4:
       
        #TRY CONDITION
        try:
            id1 = int(input("Enter your ID: "))
        except ValueError:
            print("ENTER NUMBERS NOT ALPHABETS OR OTHER")
            print()
            continue
        
        #ASKING USER INPUT ABOUT PASWORD
        pass_code = input("Enter your Password: ")

        found = False

        #FOR LOOP
        for i in employee:

            # IF ELSE CONDITION
            if i["Id"] == id1 and i["Password"] == pass_code:

                #WHILE LOOP
                while True:

                    #TABLE
                    print("+--------------------------------+")
                    print("| 1 | CHANGE NAME                |")
                    print("---------------------------------")
                    print("| 2 | CHANGE AGE                 |")
                    print("---------------------------------")
                    print("| 3 | CHANGE DEPARTMENT          |")
                    print("---------------------------------")
                    print("| 4 | CHANGE JOB                 |")
                    print("---------------------------------")
                    print("| 5 | CHANGE YEARS OF EXPERIENCE |")
                    print("---------------------------------")
                    print("| 6 | CHANGE ID                  |")
                    print("---------------------------------")
                    print("| 7 | CHANGE PASSWORD            |")
                    print("---------------------------------")
                    print("| 8 | CHANGE ALL                 |")
                    print("---------------------------------")
                    print("| 0 | EXIT                       |")
                    print("+--------------------------------+")

                    #ASKING THE USER THE INPUT
                    try:
                        ask = int(input("ENTER YOU CHOICE: "))
                    except ValueError:
                        print("Please Number not Alphabet or Other")
                        print()
                        continue
                    
                    #IF ELSE CONDITION(CHANING NAME)
                    if ask == 1:

                        # HEADING
                        print("CHANGE NAME")
                        print("````````````")
                        print()

                        # ASKING USER THE INPUT OF NAME AND SAVE IT
                        name2 = input("ENTER YOUR NAME: ")
                        i["Name"] = name2
                        print()
                        print("Data Saved Successfully")
                        print()

                    #IF ELSE CONDITION(CHANGING AGE)
                    elif ask == 2:
                        
                        #HEADING
                        print("CHANGE AGE")
                        print("```````````")
                        print()

                        #TRY CONDITION(USING TRY CONDITION ASKING INPUT AND SAVING IT )
                        try:
                             age1 = int(input("ENTER YOUR AGE: "))
                             print()
                        except ValueError:
                            print("USE NUMBERS NOT ALPHABESTS OR OTHERS")
                            print()
                            continue

                        i["Age"] = age1
                        print("Data Saved Successfully")
                        print()

                    # IF ELSE CONDITION(CHANGING DEPARTMENT)
                    elif ask == 3:

                        #HEADING
                        print("CHANGE DEPARTMENT")
                        print("`````````````````")
                        print()

                        # ASKING USER ABOUT DEPARTMENT AND SAVING IT
                        depart = input("WHICH DEPARTMENT YOU ARE: ")
                        i["Department"] = depart
                        print()
                        print("Data Saved Successfully")
                        print()

                    # IF ELSE CONDITION(CHANGING JOB)
                    elif ask == 4:

                        #HEADING
                        print("CHANGE JOB")
                        print("``````````")
                        print()

                        # ASKING USER WHICH JOB AS INPUT AND SAVING IT
                        job1 = input("ENTER YOU JOB: ")
                        i["Job"] = job1
                        print()
                        print("Data Saved Successfully")
                        print()

                    #IF ELSE CONDITION(CHANGING YEARS OF EXPERIENCE)
                    elif ask == 5:

                        #HEADING
                        print("CHANGE YEARS OF EXPERIENCE")
                        print("``````````````````````````")
                        print()

                        try:
                            exp = int(input("ENTER YOUR NUMBER OF YEARS OF EXPERIENCE: "))
                            print()
                        except ValueError:
                            print("Please Enter Numbers not Alphabets or Others")
                            print()
                            continue

                        # SAVING THE NEW INPUT
                        i["Experience"] = exp
                        print("Data Saved Successfully")
                        print()

                    # IF ELSE CONDITION(CHANGING ID)
                    elif ask == 6:

                        #HEADING
                        print("CHANGE ID")
                        print("`````````")
                        print()

                        #TRY CONDITIOM(USING TRY CONDITION ASKING USER NEW ID)
                        try:
                            id2 = int(input("ENTER YOUR ID: "))
                            print()
                        except ValueError:
                            print("Please enter Numbers not Alphabets or Others")
                            print()
                            continue

                        # SAVING NEW ID
                        i["Id"] = id2
                        print("Data Saved Successfully")

                    #IF ELSE CONDITION(CHANGING PASSWORD)
                    elif ask == 7:
                        #HEADING
                        print("CHANGE PASSWORD")
                        print("```````````````")
                        print()

                        #ASKING USER ABOUT NEW PASSWORD
                        new_pass1 = input("ENTER YOUR NEW PASSWORD: ")

                        #SAVING NEW PASSWORD AND TELL USER THAT DATA SAVED SUCCESSFULLY
                        i["Password"] = new_pass1
                        print()
                        print("Data Saved Successfully")
                        print()

                    # IF ELSE CONDITION(CHANGING ALL PERSONAL DETAILS)
                    elif ask == 8:

                        #HEADING
                        print("CHANGE ALL YOUR PERSONAL DETAILS")
                        print("````````````````````````````````")

                        #ASKING NEW NAME AND SAVING IT
                        nam1 = input("Enter Your Name: ")
                        i["Name"] = nam1
                        print("Data Saved Successfuly")
                        print()

                        # TRY CONDITION(USING TRY CONDITION ASKING USER ABOUT NEW AGE AS INPUT)
                        try:
                            age2 = int(input("Enter your Age: "))
                            print()
                        except ValueError:
                            print("Please enter Number not Alphabets or Others")
                            print()
                            continue

                        # SAVING NEW AGE
                        i["Age"] = age2
                        print("Data Saved Successfully")
                        print()

                        # ASKING USER NEW INPUT ABOUT DEPARTMENT AND SAVING IT
                        dep2 = input("Enter Your Department: ")
                        i["Department"] = dep2
                        print()
                        print("Data Saved Successfully")
                        print()

                        #ASKING USER ABOUT JOB AND SAVING IT
                        job3 = input("Enter you Job: ")
                        i["Job"]=  job3
                        print()
                        print("Data Saved Successfully")
                        print()

                        #ASKING USER ABOUT YEARS OF EXPERIENCE AND SAVE IT
                        try:
                            exp3 = int(input("Enter the number of Years of Experiences: "))
                            print()
                        except ValueError:
                            print("Please enter Number not Alphabets or Others")
                            print()
                            continue
                        
                        #SAVING DATA AND PRINTING DATA SAVED SUCCESSFULLY
                        i["Experience"] = exp3
                        print("Data Saved Successfully")
                        print()

                        #ASKING USER ABOUT NEW ID AND SAVE IT
                        try:
                            id5 = int(input("Enter your ID: "))
                            print()
                        except ValueError:
                            print("Please enter number not Alphabets or Other")
                            print()
                            continue
                        #SAVING DATA AND PRINTING DATA SAVED SUCCESSFULLY
                        i["Id"] = id5
                        print("Data Saved Successfully")
                        print()

                        #ASKING USER ABOUT NEW PASSWORD
                        new_pass0 = input("Enter your new Password: ")
                        i["Password"] = new_pass0
                        print("Data Saved Successfully")
                        print()

                    elif ask == 0:
                        print(" THANK YOU! ")
                        break
                    else:
                        print("INVALID INPUT")
