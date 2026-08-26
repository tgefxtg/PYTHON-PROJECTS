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
# EMPTY LIST
expenses = []

for days in day :
    console.print(Panel(f"[yellow]ENTER YOU EXPERNSE FOR {days}[/yellow]",expand=False))
    amount = int(input("AMOUNT : ₹ "))
    expenses.append(amount)

# CONVERTING EXPENSE LIST INTO ARRAY
expense = np.array(expenses)

#ASKING THE USER THE INPUT ABOUT THE LIMITED AMOUNT THEY WANT TO ADD
console.print(Panel("[yellow]ENTER YOU LIMITED AMOUNT[/yellow]",expand=False))
limit = int(input("₹ "))

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