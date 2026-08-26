# STUDENT DATA ANALYZER

students = []

while True:
    print("\n+--------------------------+")
    print("| 1 | ADD STUDENT DETAILS  |")
    print("| 2 | VIEW STUDENT DETAILS |")
    print("| 3 | EXIT                 |")
    print("+--------------------------+")

    choice = input("ENTER YOUR CHOICE: ")

    if choice == "1":

        no_subject = int(input("ENTER THE NUMBER OF SUBJECTS: "))

        subjects = []

        print("\nENTER SUBJECT NAMES")
        for i in range(no_subject):
            subject = input(f"Subject {i + 1}: ")
            subjects.append(subject)

        no_student = int(input("\nENTER THE NUMBER OF STUDENTS: "))

        for i in range(no_student):

            print(f"\nENTER DETAILS OF STUDENT {i + 1}")

            name = input("Student Name: ")

            marks = {}

            total = 0

            for subject in subjects:
                mark = float(input(f"Enter marks for {subject}: "))
                marks[subject] = mark
                total += mark

            average = total / no_subject

            if average >= 90:
                grade = "A+"
            elif average >= 80:
                grade = "A"
            elif average >= 70:
                grade = "B"
            elif average >= 60:
                grade = "C"
            elif average >= 50:
                grade = "D"
            else:
                grade = "F"

            student = {
                "Name": name,
                "Marks": marks,
                "Total": total,
                "Average": average,
                "Grade": grade
            }

            students.append(student)

        print("\nStudent details saved successfully!")

    elif choice == "2":

        if len(students) == 0:
            print("\nNo student records found.")
        else:
            print("\n========== STUDENT DETAILS ==========")

            for student in students:
                print(f"\nName : {student['Name']}")

                print("Marks:")
                for subject, mark in student["Marks"].items():
                    print(f"  {subject}: {mark}")

                print(f"Total   : {student['Total']}")
                print(f"Average : {student['Average']:.2f}")
                print(f"Grade   : {student['Grade']}")
                print("-" * 35)

    elif choice == "3":
        print("\nThank you for using Student Data Analyzer.")
        break

    else:
        print("\nInvalid choice! Please try again.")