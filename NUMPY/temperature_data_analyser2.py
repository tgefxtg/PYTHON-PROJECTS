import numpy as np
from rich.console import Console
from rich.table import Table

console = Console()

table= Table(title ="TEMPERATURE DATA ANALYSER",caption_justify="center")

# MENTIONING DAYS IN ARRAY
days = np.array([
    
    "SUNDAY",
    "MONDAY",
    "TUSEDAY",
    "WENESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY"
])

# MENTIONING TEMPERATURE IN ARRAY
temperature = np.array([29,30,31,32,33,43,34])

# FINDING AVERAGE OF THE TEMPERATURE
average = np.mean(temperature)

# FINDING HIGHEST VALUE TEMPERATURE
highest_temperature = np.max(temperature)

# FINDING LOWEST VALUE OF TEMPERATURE
lowest_temperature = np.min(temperature)

# FINDING HOTTEST DAY
highest_index = np.argmax(temperature)
highest_day = days[highest_index]

# FINDNIG COLDEST DAYS
lowest_index = np.argmin(temperature)
lowest_day = days[lowest_index]

# FINDING DAYS HOTTER THAN AVERAGE
hotter_days_average = days[average < temperature]

# FINDING TEMPERATURE HOTTER THAN AVERAGE
hotter_temperature_average = temperature[average < temperature]

# DISPLAY RESULT
#-------------------#

# table formats
table.add_column("DAYS",style ="cyan", justify = "center")
table.add_column("TEMPERATURE", style="cyan", justify = "center")

for day,temp in zip(days, temperature):
    table.add_row(day,str(temp)+ "°C")
console.print(table)


table.add_row("AVERAGE", str(average))
table.add_row("HIGHEST TEMPERATURE", str(highest_temperature))
table.add_row("LOWEST TEMPERATURE", str(lowest_temperature))
table.add_row("HOTTEST DAY", highest_day)
table.add_row("COLDEST DAY", lowest_day)
table.add_row("DAYS HOTTER THAN AVERAGE", ", ".join(hotter_days_average))
table.add_row(
    "TEMPERATURES ABOVE AVERAGE",
    ", ".join(map(str, hotter_temperature_average))
)


console.print(table)