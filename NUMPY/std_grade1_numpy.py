# IMPORTING LiBRARIES 
import numpy as np
from rich.console import Console
console = Console()
# THIS IS A HEADLINE ON THIS CODE 
console.print("+---------------+", justify= "center" )
console.print("| STUDENT GRADE |", justify= "center" )
console.print("+--------------+", justify= "center" )

student = np.array(["SHONE","ARLENE","SIONA SUSAN BINU"])
marks = np.array([12,45,78])

print("+-----------------+")
print("| PASS MARK |  50 |")
print("+-----------------+")
print("| TOTAL MARK | 100|")
print("+-----------------+")

pass_mark = 50
total_marks = 100

average = np.mean(marks)
highest = np.max(marks)
lowest = np.min(marks)
pass_students = student[marks >= pass_mark]
failed_student = student[marks < pass_mark]
passed_count = np.sum(marks >= pass_mark)
pass_percentage = (passed_count/ len(student)*100)

top_index = np.argmax(marks)
top_student = student[top_index]
top_marks = marks[top_index]

# DISPLAYING THE RESULT
print()
print()
print("AVERGAE: ",average)
print("HIGHEST MARK: ", highest)
print("LOWEST MARK: ", lowest)
print("PASSED STUDENTS: ", pass_students)
print("FAIED STUDENT: ", failed_student)
print("PASS PERCENTAGE: ",pass_percentage)
print("TOP SCORES: ",top_student)
print("TOP MARKS: ",top_marks)

console.print("FINISHED (THANKYOU FOR USING OUR APP)",justify="center")