# Library
import numpy as np
from rich.console import Console
from rich.table import Table
console = Console()
table = Table(title="📊 Student Marks Report")

# HEADING
console.print("+---------------+")
console.print("| STUDENT MARKS |")
console.print("+---------------+")
# Student names
students = np.array(["Arun", "Rahul", "Akhil", "Neha", "Anu"])

# Student marks
marks = np.array([5, 2, 76, 28, 91])

# Pass mark
pass_mark = 40


# 1. Calculate average mark
average = np.mean(marks)

# 2. Find highest mark
highest = np.max(marks)

# 3. Find lowest mark
lowest = np.min(marks)

# Passed students
passed_student =  students[marks >= pass_mark]

# Failed student
failed_student = students[marks < pass_mark]

# CALCULATING TOTAL PASSED STUDENTS PERCENTAGE
passed_count = np.sum(marks >= pass_mark)
pass_percentage = (passed_count/ len(students)) * 100

# FINDING TOP SCORER
top_index = np.argmax(marks)

top_student =  students[top_index]
top_marks = marks[top_index]


# DISPLAYING RESULT

# print("+----------------------------------+")
# print("|AVERAGE MARKS: |",average)
# print("|HIGHEST MARKS: |",highest)
# print("|LOWEST MARKS: |",lowest)
# print("|PASSED MARKS: |",passed_student)
# print("|FAILED STUDENT: |",failed_student)
# print("|PASS PERCENTAGE: |", pass_percentage)
# print("|TOP SCORE: |", top_student)
# print("|TOP MARKS: |",top_index)
# print("+----------------------------------+")


# ADD COLUMNS
table.add_column("DETAILS", style="cyan", justify="left")
table.add_column("VALUE", style="green", justify="center")

# ADD ROWS
table.add_row("Average Marks", str(average))
table.add_row("Highest Marks", str(highest))
table.add_row("Lowest Marks", str(lowest))
table.add_row("Passed Students", ", ".join(passed_student))
table.add_row("Failed Students", ", ".join(failed_student))
table.add_row("Pass Percentage", f"{pass_percentage:.2f}%")
table.add_row("Top Scorer", str(top_student))
table.add_row("Top Marks", str(top_marks))

# PRINT TABLE
console.print(table)