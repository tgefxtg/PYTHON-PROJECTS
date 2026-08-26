import pandas as pd
data = [100, 101, 110, 210, 202, 220]
# in here we are converting data into series
series = pd.Series(data)
print(series)
print()

data = [100.34, 101.45, 11.220, 210.67, 202.90, 220.99]
# in here we are converting data into series
series = pd.Series(data)
print(series)
print()

data = ["A", "B", "C", "D", "E", "F"]
# in here we are converting data into series
series = pd.Series(data)
print(series)
print()

data = [True, False, True, True]
# in here we are converting data into series
series = pd.Series(data)
print(series)
print()

#NOW HERE WE ARE GOING TO ADD OR CHANGE INDEX

data = [123,456,678,890,978]
series = pd.Series(data, index =["a","b","c","d","e"])
print(series)
print()

data = [123,456,678,890,978]
series = pd.Series(data, index =["appartment - 1","appartment - 2","appartment - 3","appartment - 4","appartment - 5"])
print(series)
print()


# in here we using loc(location) and print only the mentioned index
data = [123,456,678,890,978]
series = pd.Series(data, index =["a","b","c","d","e"])
print(series.loc["c"])
data = [123,456,678,890,978]
series = pd.Series(data, index =["a","b","c","d","e"])
print(series.loc["a"])
data = [123,456,678,890,978]
series = pd.Series(data, index =["a","b","c","d","e"])
print(series.loc["e"])
print()


