# Library
import numpy as np
from rich.console import Console
from rich.table import Table

# Create Console
console = Console()

# Create Table
table = Table(title="📊 Student Marks Report")

# Heading
console.print("+---------------+", justify="center")
console.print("[bold cyan]| STUDENT MARKS |[/bold cyan]", justify="center")
console.print("+---------------+", justify="center")

# Student Names
students = np.array(["Arun", "Rahul", "Akhil", "Neha", "Anu"])

# Student Marks
marks = np.array([5, 2, 76, 28, 91])

# Pass Mark
pass_mark = 40

# Average
average = np.mean(marks)

# Highest
highest = np.max(marks)

# Lowest
lowest = np.min(marks)

# Passed Students
passed_student = students[marks >= pass_mark]

# Failed Students
failed_student = students[marks < pass_mark]

# Pass Percentage
passed_count = np.sum(marks >= pass_mark)
pass_percentage = (passed_count / len(students)) * 100

# Top Scorer
top_index = np.argmax(marks)
top_student = students[top_index]
top_marks = marks[top_index]

# Table Columns
table.add_column("DETAILS", style="cyan", justify="left")
table.add_column("VALUE", style="green", justify="center")

# Table Rows
table.add_row("Average Marks", str(average))
table.add_row("Highest Marks", str(highest))
table.add_row("Lowest Marks", str(lowest))
table.add_row("Passed Students", ", ".join(passed_student))
table.add_row("Failed Students", ", ".join(failed_student))
table.add_row("Pass Percentage", f"{pass_percentage:.2f}%")
table.add_row("Top Scorer", str(top_student))
table.add_row("Top Marks", str(top_marks))

# Print Table
console.print(table)