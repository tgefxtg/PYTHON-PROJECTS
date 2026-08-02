import pandas as pd

df = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9]], columns = ["A","B","C"])

# here we are printing the matrix
print(df.head())
print()

# here we are printing first 2 rows 
print(df.head(2))
print()

# here we are running last 1 row
print(df.tail(1))
print()

# here we getting the information about columns ("A","B","C")
print(df.columns)
print()

# here we printing the columns
print(df.index.tolist())
print()

# here we giving matrix as 1,2,3,4,5,6,7,8,9 and rows as A,B,C and index(first columns) as x,y,z
df = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9]], columns = ["A","B","C"], index=["x","y","z"])
print(df)
print()

# asking pandas for the index
print(df.index)
print()

# looking information of data frames 
print(df.info())

# asking meaningfull information of data 
print(df.describe())
print()
