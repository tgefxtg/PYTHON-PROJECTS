import numpy as np

# Student names
students = np.array(["Arun", "Rahul", "Akhil", "Neha", "Anu"])

# Student marks
marks = np.array([85, 42, 76, 28, 91])

# Pass mark
pass_mark = 40


# 1. Calculate average mark
average = np.mean(marks)

# 2. Find highest mark
highest = np.max(marks)

# 3. Find lowest mark
lowest = np.min(marks)


# 4. Find passed students
passed_students = students[marks >= pass_mark]

# 5. Find failed students
failed_students = students[marks < pass_mark]


# 6. Calculate pass percentage
passed_count = np.sum(marks >= pass_mark)

pass_percentage = (passed_count / len(students)) * 100


# 7. Find top scorer
top_index = np.argmax(marks)

top_student = students[top_index]
top_mark = marks[top_index]


# Display results

print("STUDENT MARKS ANALYZER")
print("----------------------")

print("Average Mark:", average)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)

print("Passed Students:", passed_students)
print("Failed Students:", failed_students)

print("Pass Percentage:", pass_percentage, "%")

print("Top Scorer:", top_student)
print("Top Mark:", top_mark)
