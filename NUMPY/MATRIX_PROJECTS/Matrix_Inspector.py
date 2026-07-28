import numpy as np
from rich.console import Console
from rich.align import Align
from rich.panel import Panel
from rich.table import Table


console = Console()
table = Table()

title = Panel("[red]MATRIX INSPECTOR[/red]",expand= False)
console.print(Align.center(title))

console.print(Panel("[yellow]ENTER YOUR MATRIX INFORMATIONS[/yellow]",expand = False ))
print()
print()

a = int(input("ENTER YOUR MATRIX [_,0]: "))
b = int(input("ENTER YOUR MATRIX [0,_]: "))
c = int(input("ENTER YOUR MATRIX [1,_]: "))
d = int(input("ENTER YOUR MATRIX [_,1]: "))
print()
print()

matrix = np.array([
    [a, b],
    [c, d]
])

shape = matrix.shape
ndim = matrix.ndim
size = matrix.size
dtype = matrix.dtype

console.print(Panel("[yellow]TABLE[/yellow]",expand=False))

table.add_column("NAME",style = "green", justify= "left")
table.add_column("MATRIX", style= "green", justify= "center")
table.add_row("SHAPE", str(shape))
table.add_row("DIMENSIONS",str(ndim))
table.add_row("SIZE",str(size))
table.add_row("DTYPE",str(dtype))

console.print(table)