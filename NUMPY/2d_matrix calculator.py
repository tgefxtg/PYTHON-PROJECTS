import numpy as np 
from rich.console import Console
from rich.table import Table
from rich.align import Align
from rich.panel import Panel

console = Console()
table = Table()


title =  Panel("[red] 2D MATRIX CALCULATOR [/red]",expand = False)
console.print(Align.center(title))

console.print(Panel("[green]MATRIX_A[/green]",expand=False))
a = int(input("ENTER YOUR NUMBER [ ,0]: "))
b = int(input("ENTER YOUR NUMBER [0, ]: "))
c = int(input("ENTER YOUR NUMBER [1, ]: "))
d = int(input("ENTER YOU NUMBER [ ,1]: "))

matrix_a = np.array([
    [a, b],
    [c, d]
])

console.print(Panel("[green]MATRIX_B[/green]",expand=False))
e = int(input("ENTER YOUR NUMBER [ ,0]: "))
f = int(input("ENTER YOUR NUMBER [0, ]: "))
g = int(input("ENTER YOUR NUMBER [1, ]: "))
h = int(input("ENTER YOU NUMBER [ ,1]: "))

matrix_b = np.array([
    [e, f],
    [g, h]
])

# CALCULATIONS

addition = matrix_a + matrix_b
subtraction = matrix_a - matrix_b
element_multiplication = matrix_a * matrix_b
matrix_multiplication = matrix_a @ matrix_b
transpose_a = matrix_a.T
transpose_b = matrix_b.T
shape_a = matrix_a.shape
shape_b = matrix_b.shape

# DISPLAYING THE RESULT :
   # displaying the matrix 
print(matrix_a)
print(matrix_b)

   # displaying 
matrix_table = Table()
matrix_table.add_column("CALCULATIONS",style="red",justify= "left")
matrix_table.add_column("RESULT", style="red", justify= "center" )
matrix_table.add_row("ADDITION",str(addition))
matrix_table.add_row("SUBTRACTION",str(subtraction))
matrix_table.add_row("ELEMENT MULTIPLICATION",str(element_multiplication))
matrix_table.add_row("MATRIX MULTIPLICATION",str(matrix_multiplication))
matrix_table.add_row("TRANSPOSE OF MATRIX_A",str(transpose_a))
matrix_table.add_row("TRANSPOSE OF MATRIX_B",str(transpose_b))
matrix_table.add_row("SHAPE OF MATRIX_A",str(shape_a))
matrix_table.add_row("TRANSPOSE OF SHAPE_A",str(shape_b))
console.print(matrix_table)
