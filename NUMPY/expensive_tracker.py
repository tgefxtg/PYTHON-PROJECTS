# IMPORTING LIBRARIES
import numpy as np
from rich.console import Console
from rich.align import Align
from rich.table import Table
from rich.panel import Panel

console = Console()
table = Table()

# GIVING HEADING 
heading = Panel(
    "[bold green]EXPENSE TRACKER[/bold green]",
    expand=False
)

# MENTIONING THE DAYS IN VARIABLE 
day = np.array(["SUNDAY",
                 "MODAY",
                 "TUSEDAY",
                 "WENESDAY",
                 "THURSDAY",
                 "FRIDAY",
                 "SATURDAY"])

# MENTIONING THE EXPENSE IN VARIABLES
expense = np.array([234,566,134,978,876,654,423])

# MENTIONING THE LIMIT OF EXPERNSE AS A VARIABLE
limit = 700

# FINDING THE SUM OF THE EXPENSE
sum = np.sum(expense)

#FINDING THE MEAN(AVERAGE OF THE SUM)
average = np.mean(expense)

# FINDING THE MAX AMOUNT SPEND ON EXPENSE
max = np.max(expense)
# FINDING THE MINIMUM AMOUNT SPEND ON EXPENSE
min =  np.min(expense)

# FINDING THE DAYS WITH HIGHEST EXPENSE
highest = np.argmax(expense)
highest_expense_day = day[highest]

# DAYS WHERE SPENDING CROSSED THE LIMIT
highest_day = day[expense > limit]

# EXPENSE WHERE SPENDING CROSSED THE LIMIT
highest_expense = expense[expense > limit]


# DISPLAY THE RESULT
#===================#
expense_table = Table()
expense_table.add_column("DAY", style="red", justify="left")
expense_table.add_column("EXPENSE", style="red", justify= "left")
for days,expenses in zip(day, expense):
    expense_table.add_row(days,str(expenses))
console.print(Align.center(heading))
print()
print()
console.print(expense_table)
print()
print()

calculation_table = Table()
calculation_table.add_column("[green]CALCULATION[/green]", style="red", justify="left")
calculation_table.add_column("[green]EXPENSE[/green]", style="red", justify= "left")
calculation_table.add_row("SUM OF EXPENSE",str(sum))
calculation_table.add_row("AVERAGE OF EXPENSE", str(average))
calculation_table.add_row("HIGHEST AMOUNT SPEND", str(max))
calculation_table.add_row("LOWEST AMOUNT SPEND", str(min))
calculation_table.add_row("HIGHEST AMOUNT SPEND DAY",(highest_expense_day))
calculation_table.add_row("EXPENSE USED MORE THAN THE LIMIT", ",".join (map(str,highest_expense)))
console.print(calculation_table)