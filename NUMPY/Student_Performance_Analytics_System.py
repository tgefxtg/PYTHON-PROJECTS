import numpy as np
from rich.console import Console
from rich.table import Table
from rich.align import Align
from rich.panel import Panel

console = Console()


title = Panel(
    "[bold yellow]STUDENT PERFORMANCE ANALYSIS[/bold yellow]",
    expand=False
)
console.print(Align.center(title))



while True:

    try:
        student_count = int(
            input("\nHow many students?: ")
        )

        subject_count = int(
            input("How many subjects?: ")
        )

        if student_count > 0 and subject_count > 0:
            break

        console.print(
            "[red]Students and subjects must be greater than 0.[/red]"
        )

    except ValueError:
        console.print(
            "[red]Please enter whole numbers only.[/red]"
        )

student_names = []
subject_names = []
all_marks = []


title_subject_name = Panel(
    "[bold green]ENTER SUBJECT NAMES[/bold green]",
    expand=False
)

console.print()
console.print(Align.center(title_subject_name))


for i in range(subject_count):

    while True:

        subject = input(
            f"Enter subject {i + 1} name: "
        ).strip()

        if subject:
            subject_names.append(subject)
            break

        console.print(
            "[red]Subject name cannot be empty.[/red]"
        )


title_student_details = Panel(
    "[bold green]ENTER STUDENT DETAILS & MARKS[/bold green]",
    expand=False
)

console.print()
console.print(Align.center(title_student_details))


for i in range(student_count):

    # Get student name
    while True:

        name = input(
            f"\nEnter student {i + 1} name: "
        ).strip()

        if name:
            student_names.append(name)
            break

        console.print(
            "[red]Student name cannot be empty.[/red]"
        )

    # Store marks of current student
    student_marks = []

    for j in range(subject_count):

        while True:

            try:

                mark = float(
                    input(
                        f"Enter {name}'s mark for "
                        f"{subject_names[j]}: "
                    )
                )

                if 0 <= mark <= 100:
                    break

                console.print(
                    "[red]Mark must be between 0 and 100.[/red]"
                )

            except ValueError:

                console.print(
                    "[red]Please enter a valid number.[/red]"
                )

        student_marks.append(mark)

    # Add current student's marks
    # to main marks list
    all_marks.append(student_marks)


marks = np.array(
    all_marks,
    dtype=float
)


student_totals = np.sum(
    marks,
    axis=1
)

student_averages = np.mean(
    marks,
    axis=1
)

student_highest = np.max(
    marks,
    axis=1
)

student_lowest = np.min(
    marks,
    axis=1
)


subject_averages = np.mean(
    marks,
    axis=0
)



best_student_index = np.argmax(
    student_averages
)

best_student = student_names[
    best_student_index
]


hardest_subject_index = np.argmin(
    subject_averages
)

hardest_subject = subject_names[
    hardest_subject_index
]




title_student_result = Panel(
    "[bold green]STUDENT RESULTS[/bold green]",
    expand=False
)

console.print()
console.print(Align.center(title_student_result))


result_table = Table(
    title="Student Performance"
)

result_table.add_column(
    "Student",
    style="cyan"
)

result_table.add_column(
    "Total",
    justify="center"
)

result_table.add_column(
    "Average",
    justify="center"
)

result_table.add_column(
    "Highest",
    justify="center"
)

result_table.add_column(
    "Lowest",
    justify="center"
)


for i in range(student_count):

    result_table.add_row(
        student_names[i],
        f"{student_totals[i]:.2f}",
        f"{student_averages[i]:.2f}",
        f"{student_highest[i]:.2f}",
        f"{student_lowest[i]:.2f}"
    )


console.print(result_table)



title_subject_average = Panel(
    "[bold green]SUBJECT AVERAGES[/bold green]",
    expand=False
)

console.print()
console.print(Align.center(title_subject_average))


subject_table = Table()

subject_table.add_column(
    "Subject",
    style="cyan"
)

subject_table.add_column(
    "Average",
    justify="center"
)


for i in range(subject_count):

    subject_table.add_row(
        subject_names[i],
        f"{subject_averages[i]:.2f}"
    )


console.print(subject_table)



title_class_analysis = Panel(
    "[bold green]CLASS ANALYSIS[/bold green]",
    expand=False
)

console.print()
console.print(Align.center(title_class_analysis))


console.print(
    f"\nBest Student: "
    f"[bold cyan]{best_student}[/bold cyan] "
    f"({student_averages[best_student_index]:.2f})"
)


console.print(
    f"Hardest Subject: "
    f"[bold yellow]{hardest_subject}[/bold yellow] "
    f"({subject_averages[hardest_subject_index]:.2f})"
)



title_marks_matrix = Panel(
    "[bold green]MARKS MATRIX[/bold green]",
    expand=False
)

console.print()
console.print(Align.center(title_marks_matrix))


matrix_table = Table()

matrix_table.add_column(
    "Student",
    style="cyan"
)


# Add subject columns
for subject in subject_names:

    matrix_table.add_column(
        subject,
        justify="center"
    )


# Add student marks
for i in range(student_count):

    row = [
        student_names[i]
    ]

    for mark in marks[i]:

        row.append(
            f"{mark:.2f}"
        )

    matrix_table.add_row(
        *row
    )


console.print(matrix_table)



title_analysis_complete = Panel(
    "[bold green]ANALYSIS COMPLETE[/bold green]",
    expand=False
)

console.print()
console.print(
    Align.center(title_analysis_complete)
)