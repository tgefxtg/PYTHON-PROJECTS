import numpy as np



# Days of the week
days = np.array([
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
])

# Temperature for each day in Celsius
temperatures = np.array([31, 33, 32, 35, 34, 30, 29])


#Average temperature
average = np.mean(temperatures)

#Highest temperature
highest = np.max(temperatures)

#Lowest temperature
lowest = np.min(temperatures)


#Find hottest day
hottest_index = np.argmax(temperatures)
hottest_day = days[hottest_index]


#Find coldest day
coldest_index = np.argmin(temperatures)
coldest_day = days[coldest_index]


#Find days hotter than average
hot_days = days[temperatures > average]

#Find temperatures above average
hot_temperatures = temperatures[temperatures > average]


# DISPLAYING THE RESULT
print()

print("+---------------------------+")
print("| TEMPERATURE DATA ANALYZER |")
print("+---------------------------+")

print()
print()
print()

print("+-------------------------------------------------------------+")
print("|Average Temperature:       |", average, "°C                         |")
print("|Highest Temperature:       |", highest, "  °C                         |")
print("|Lowest Temperature:        |", lowest, "  °C                         |")

print("|Hottest Day:               |", hottest_day,"                       |")
print("|Coldest Day:               |", coldest_day,"                         |")

print("|Days Above Average:        |", hot_days,"|")
print("|Temperatures Above Average:|", hot_temperatures,"                     |")
print("+-------------------------------------------------------------+")
