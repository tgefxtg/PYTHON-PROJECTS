import numpy as np

# --------------------------------
# STUDENT PERFORMANCE ANALYZER
# --------------------------------

print("\n===== STUDENT PERFORMANCE ANALYZER =====\n")

# 1. Ask how many students and subjects
student_count = int(input("How many students? "))
subject_count = int(input("How many subjects? "))

# Lists for storing names and marks
student_names = []
subject_names = []
all_marks = []


# --------------------------------
# 2. Get subject names
# --------------------------------

print("\n--- ENTER SUBJECT NAMES ---")

for i in range(subject_count):
    subject = input(f"Enter subject {i + 1} name: ")
    subject_names.append(subject)


# --------------------------------
# 3. Get student names and marks
# --------------------------------

print("\n--- ENTER STUDENT DETAILS ---")

for i in range(student_count):

    name = input(f"\nEnter student {i + 1} name: ")
    student_names.append(name)

    student_marks = []

    for j in range(subject_count):

        mark = float(
            input(f"Enter {name}'s mark for {subject_names[j]}: ")
        )

        student_marks.append(mark)

    all_marks.append(student_marks)


# --------------------------------
# 4. Convert marks into NumPy array
# --------------------------------

marks = np.array(all_marks)


# --------------------------------
# 5. Student statistics
# --------------------------------

student_totals = np.sum(marks, axis=1)

student_averages = np.mean(marks, axis=1)

student_highest = np.max(marks, axis=1)

student_lowest = np.min(marks, axis=1)


# --------------------------------
# 6. Subject statistics
# --------------------------------

subject_averages = np.mean(marks, axis=0)


# --------------------------------
# 7. Best student
# --------------------------------

best_student_index = np.argmax(student_averages)

best_student = student_names[best_student_index]


# --------------------------------
# 8. Hardest subject
# --------------------------------

hardest_subject_index = np.argmin(subject_averages)

hardest_subject = subject_names[hardest_subject_index]


# --------------------------------
# 9. Display student results
# --------------------------------

print("\n\n===== STUDENT RESULTS =====")

for i in range(student_count):

    print(f"\nStudent: {student_names[i]}")

    print(f"Total: {student_totals[i]}")
    print(f"Average: {student_averages[i]:.2f}")
    print(f"Highest Mark: {student_highest[i]}")
    print(f"Lowest Mark: {student_lowest[i]}")


# --------------------------------
# 10. Display subject averages
# --------------------------------

print("\n===== SUBJECT AVERAGES =====")

for i in range(subject_count):

    print(
        f"{subject_names[i]}: "
        f"{subject_averages[i]:.2f}"

    )


# --------------------------------
# 11. Final analysis
# --------------------------------

print("\n===== CLASS ANALYSIS =====")

print(f"Best Student: {best_student}")

print(f"Hardest Subject: {hardest_subject}")


