import numpy as np
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align

console = Console()


# ============================================================
# TITLE
# ============================================================

def show_title():
    title = Panel(
        "[bold cyan]MATRIX EXPLORER[/bold cyan]\n"
        "[dim]Explore • Analyze • Calculate[/dim]",
        expand=False
    )
    console.print(Align.center(title))


def create_matrix(name="Matrix"):

    console.print(f"\n[bold yellow]Create {name}[/bold yellow]")

    while True:
        try:
            rows = int(input("Enter number of rows: "))
            columns = int(input("Enter number of columns: "))

            if rows <= 0 or columns <= 0:
                console.print("[red]Rows and columns must be greater than 0.[/red]")
                continue

            break

        except ValueError:
            console.print("[red]Please enter valid integers.[/red]")

    matrix = []

    console.print(
        f"\nEnter {columns} values for each row."
    )

    for i in range(rows):

        while True:
            try:
                values = list(
                    map(
                        float,
                        input(f"Row {i + 1}: ").split()
                    )
                )

                if len(values) != columns:
                    console.print(
                        f"[red]Enter exactly {columns} values.[/red]"
                    )
                    continue

                matrix.append(values)
                break

            except ValueError:
                console.print(
                    "[red]Only numbers are allowed.[/red]"
                )

    return np.array(matrix, dtype=float)


def display_matrix(matrix, name="Matrix"):

    table = Table(
        title=name,
        show_header=True,
        header_style="bold magenta"
    )

    for column in range(matrix.shape[1]):
        table.add_column(
            f"C{column + 1}",
            justify="center"
        )

    for row in matrix:
        table.add_row(
            *[f"{value:.2f}" for value in row]
        )

    console.print(table)


def matrix_information(matrix):

    rows, columns = matrix.shape

    table = Table(
        title="Matrix Information",
        show_header=True
    )

    table.add_column("Property", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Rows", str(rows))
    table.add_row("Columns", str(columns))
    table.add_row("Shape", str(matrix.shape))
    table.add_row("Size", str(matrix.size))
    table.add_row("Dimensions", str(matrix.ndim))
    table.add_row("Data Type", str(matrix.dtype))

    if rows == columns:
        matrix_type = "Square Matrix"
    else:
        matrix_type = "Rectangular Matrix"

    table.add_row("Matrix Type", matrix_type)

    console.print(table)



def matrix_statistics(matrix):

    table = Table(title="Matrix Statistics")

    table.add_column("Operation", style="cyan")
    table.add_column("Result", style="green")

    table.add_row("Sum", f"{np.sum(matrix):.2f}")
    table.add_row("Mean", f"{np.mean(matrix):.2f}")
    table.add_row("Minimum", f"{np.min(matrix):.2f}")
    table.add_row("Maximum", f"{np.max(matrix):.2f}")
    table.add_row("Standard Deviation", f"{np.std(matrix):.2f}")
    table.add_row("Variance", f"{np.var(matrix):.2f}")

    console.print(table)


def determinant(matrix):

    if matrix.shape[0] != matrix.shape[1]:
        console.print(
            "[red]Determinant requires a square matrix.[/red]"
        )
        return

    det = np.linalg.det(matrix)

    console.print(
        f"\n[cyan]Determinant:[/cyan] [green]{det:.4f}[/green]"
    )

def inverse(matrix):

    if matrix.shape[0] != matrix.shape[1]:
        console.print(
            "[red]Inverse requires a square matrix.[/red]"
        )
        return

    try:
        result = np.linalg.inv(matrix)

        display_matrix(
            result,
            "Inverse Matrix"
        )

    except np.linalg.LinAlgError:
        console.print(
            "[red]Inverse does not exist. Matrix is singular.[/red]"
        )


def transpose(matrix):

    result = matrix.T

    display_matrix(
        result,
        "Transpose"
    )


def matrix_rank(matrix):

    rank = np.linalg.matrix_rank(matrix)

    console.print(
        f"\n[cyan]Matrix Rank:[/cyan] [green]{rank}[/green]"
    )



def matrix_trace(matrix):

    if matrix.shape[0] != matrix.shape[1]:

        console.print(
            "[red]Trace requires a square matrix.[/red]"
        )

        return

    trace = np.trace(matrix)

    console.print(
        f"\n[cyan]Trace:[/cyan] [green]{trace:.2f}[/green]"
    )



def eigen(matrix):

    if matrix.shape[0] != matrix.shape[1]:

        console.print(
            "[red]Eigenvalues require a square matrix.[/red]"
        )

        return

    values, vectors = np.linalg.eig(matrix)

    console.print(
        "\n[bold cyan]Eigenvalues[/bold cyan]"
    )

    console.print(values)

    console.print(
        "\n[bold cyan]Eigenvectors[/bold cyan]"
    )

    console.print(vectors)



def add_matrices(matrix):

    console.print(
        "\n[yellow]Create Matrix B[/yellow]"
    )

    matrix_b = create_matrix("Matrix B")

    if matrix.shape != matrix_b.shape:

        console.print(
            "[red]Matrices must have the same shape.[/red]"
        )

        return

    result = matrix + matrix_b

    display_matrix(
        result,
        "A + B"
    )


def subtract_matrices(matrix):

    matrix_b = create_matrix("Matrix B")

    if matrix.shape != matrix_b.shape:

        console.print(
            "[red]Matrices must have the same shape.[/red]"
        )

        return

    result = matrix - matrix_b

    display_matrix(
        result,
        "A - B"
    )



def multiply_matrices(matrix):

    matrix_b = create_matrix("Matrix B")

    if matrix.shape[1] != matrix_b.shape[0]:

        console.print(
            "[red]"
            "Matrix multiplication not possible.\n"
            "Columns of A must equal rows of B."
            "[/red]"
        )

        return

    result = matrix @ matrix_b

    display_matrix(
        result,
        "A × B"
    )



def elementwise_multiplication(matrix):

    matrix_b = create_matrix("Matrix B")

    if matrix.shape != matrix_b.shape:

        console.print(
            "[red]Matrices must have the same shape.[/red]"
        )

        return

    result = matrix * matrix_b

    display_matrix(
        result,
        "A * B (Element-wise)"
    )



def scalar_multiplication(matrix):

    try:

        scalar = float(
            input("Enter scalar value: ")
        )

        result = matrix * scalar

        display_matrix(
            result,
            f"Matrix × {scalar}"
        )

    except ValueError:

        console.print(
            "[red]Invalid scalar value.[/red]"
        )



def row_column_analysis(matrix):

    console.print(
        "\n[bold cyan]Row Sums[/bold cyan]"
    )

    for i, value in enumerate(
        np.sum(matrix, axis=1)
    ):
        console.print(
            f"Row {i + 1}: {value:.2f}"
        )

    console.print(
        "\n[bold cyan]Column Sums[/bold cyan]"
    )

    for i, value in enumerate(
        np.sum(matrix, axis=0)
    ):
        console.print(
            f"Column {i + 1}: {value:.2f}"
        )

    console.print(
        "\n[bold cyan]Row Means[/bold cyan]"
    )

    for i, value in enumerate(
        np.mean(matrix, axis=1)
    ):
        console.print(
            f"Row {i + 1}: {value:.2f}"
        )

    console.print(
        "\n[bold cyan]Column Means[/bold cyan]"
    )

    for i, value in enumerate(
        np.mean(matrix, axis=0)
    ):
        console.print(
            f"Column {i + 1}: {value:.2f}"
        )



def special_matrix_checker(matrix):

    rows, columns = matrix.shape

    console.print(
        "\n[bold cyan]Matrix Type Analysis[/bold cyan]"
    )

    if rows == columns:
        console.print("[green]✓ Square Matrix[/green]")
    else:
        console.print("[yellow]✓ Rectangular Matrix[/yellow]")

    if np.all(matrix == 0):
        console.print("[green]✓ Zero Matrix[/green]")

    if rows == columns:

        if np.array_equal(
            matrix,
            np.eye(rows)
        ):
            console.print(
                "[green]✓ Identity Matrix[/green]"
            )

        if np.allclose(
            matrix,
            np.diag(np.diagonal(matrix))
        ):
            console.print(
                "[green]✓ Diagonal Matrix[/green]"
            )

        if np.allclose(
            matrix,
            matrix.T
        ):
            console.print(
                "[green]✓ Symmetric Matrix[/green]"
            )

        if np.allclose(
            matrix,
            np.triu(matrix)
        ):
            console.print(
                "[green]✓ Upper Triangular Matrix[/green]"
            )

        if np.allclose(
            matrix,
            np.tril(matrix)
        ):
            console.print(
                "[green]✓ Lower Triangular Matrix[/green]"
            )



def show_menu():

    table = Table(
        title="Matrix Explorer Menu"
    )

    table.add_column(
        "Option",
        justify="center",
        style="cyan"
    )

    table.add_column(
        "Operation",
        style="yellow"
    )

    table.add_row("1", "Display Matrix")
    table.add_row("2", "Matrix Information")
    table.add_row("3", "Matrix Statistics")
    table.add_row("4", "Transpose")
    table.add_row("5", "Determinant")
    table.add_row("6", "Inverse")
    table.add_row("7", "Rank")
    table.add_row("8", "Trace")
    table.add_row("9", "Eigenvalues / Eigenvectors")
    table.add_row("10", "Add Matrix")
    table.add_row("11", "Subtract Matrix")
    table.add_row("12", "Matrix Multiplication")
    table.add_row("13", "Element-wise Multiplication")
    table.add_row("14", "Scalar Multiplication")
    table.add_row("15", "Row / Column Analysis")
    table.add_row("16", "Special Matrix Checker")
    table.add_row("17", "Create New Matrix")
    table.add_row("0", "Exit")

    console.print(table)



def main():

    show_title()

    console.print(
        "\n[bold green]Create your first matrix[/bold green]"
    )

    matrix = create_matrix("Matrix A")

    while True:

        console.print()

        show_menu()

        try:
            choice = int(
                input("\nChoose an option: ")
            )

        except ValueError:
            console.print(
                "[red]Please enter a number.[/red]"
            )
            continue

        console.print()

        if choice == 1:

            display_matrix(
                matrix,
                "Matrix A"
            )

        elif choice == 2:

            matrix_information(matrix)

        elif choice == 3:

            matrix_statistics(matrix)

        elif choice == 4:

            transpose(matrix)

        elif choice == 5:

            determinant(matrix)

        elif choice == 6:

            inverse(matrix)

        elif choice == 7:

            matrix_rank(matrix)

        elif choice == 8:

            matrix_trace(matrix)

        elif choice == 9:

            eigen(matrix)

        elif choice == 10:

            add_matrices(matrix)

        elif choice == 11:

            subtract_matrices(matrix)

        elif choice == 12:

            multiply_matrices(matrix)

        elif choice == 13:

            elementwise_multiplication(matrix)

        elif choice == 14:

            scalar_multiplication(matrix)

        elif choice == 15:

            row_column_analysis(matrix)

        elif choice == 16:

            special_matrix_checker(matrix)

        elif choice == 17:

            matrix = create_matrix(
                "New Matrix A"
            )

            console.print(
                "[green]Matrix replaced successfully![/green]"
            )

        elif choice == 0:

            console.print(
                "\n[bold green]"
                "Thanks for using Matrix Explorer!"
                "[/bold green]"
            )

            break

        else:

            console.print(
                "[red]Invalid option.[/red]"
            )



if __name__ == "__main__":
    main()