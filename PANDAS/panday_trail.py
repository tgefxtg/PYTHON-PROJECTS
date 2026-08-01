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

