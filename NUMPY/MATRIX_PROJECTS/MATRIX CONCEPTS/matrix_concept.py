print("+----+")
print("|SETS|")
print("+----+")
print()

# IN THIS CODE THE PYTHON ITS MENTIONING THE NUMBER OF ROWS AND COLUMNS
import numpy as np
array = np.array([
    ['A','B','C'],
    ['D','E','F']
])
print(array.shape)
print()

# IN HERE WE ARE MENTIONING THE DIMENTIONS OF THE MATRIX
import numpy as np
array = np.array([
    [['A','B','C'],['D','E','F'],['G','H','I']],
    [['J','K','L'],['M','N','O'],['P','Q','R']],
    [['S','T','U'],['V','W','X'],['-','Y','Z']]
])
print(array.ndim)
print()

import numpy as np
array = np.array([
    [['A','B','C'],['D','E','F'],['G','H','I']],
    [['J','K','L'],['M','N','O'],['P','Q','R']],
    [['S','T','U'],['V','W','X'],['-','Y','Z']]
])
print(array.shape)
# we got output as (3,3,3)
# first 3 = is layer
# second 3 = is rows
# third 3 =  is column
print()

import numpy as np
array = np.array([
    [['A','B','C'],['D','E','F'],['G','H','I']],
    [['J','K','L'],['M','N','O'],['P','Q','R']],
    [['S','T','U'],['V','W','X'],['-','Y','Z']]
])
print(array[1][1][1])
# this means
# 1 = second layer ['J','K','L'],['M','N','O'],['P','Q','R']
# 1 = second row ['M','N','O']
# 1 = second column N
# output = N
print()

# creating words using array
import numpy as np
array = np.array([
    [['A','B','C'],['D','E','F'],['G','H','I']],
    [['J','K','L'],['M','N','O'],['P','Q','R']],
    [['S','T','U'],['V','W','X'],['-','Y','Z']]
])
word = array[2,0,0] + array[0,2,1] + array[1,1,2] + array[1,1,1] + array[0,1,1]
print(word)
print()

#ROW SELECTION

import numpy as np
array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]
])
# array = [start:end:step]
# start
print(array[0:3:1])
print()

# COLUMN SELECTION
import numpy as np
array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]
])
# array = start:end:step
print(array[:, 1])
print()

print("+----------------------------------------------+")
print("|BASIC THING LIKE ('+' , '-' , '*' , '/', '**')|")
print("+----------------------------------------------+")
print()

import numpy as np
array = np.array([1,2,3,4,5,6])
print(array+1)
print(array-23)
print(array * 34)
print(array/2)
print(array**2)
print()

# in here we are finding the squareroot of function on matrix
import numpy as np
array = np.array([2,5,6,8])
print(np.sqrt(array))
print()

# ROUND THE ARRAY
import numpy as np
array = np.array([1.2, 34.4, 56.5, 78.99])
print(np.round(array))
print()

# ROUND DOWN
import numpy as np
array =  np.array([1.2,45.5,22.9])
print(np.floor(array))
print()

# ROUND UP
import numpy as np
damn = np.array([1.2,45.5,22.9])
print(np.ceil(damn))
print()

# finding the pi
import numpy as np
print(np.pi)
print()
print()

print("+------------------------+")
print("|VECTORIZED MATH FUNCTION|")
print("+------------------------+")
print("+------------------------------------------+")
print("| TO FIND THE RADIUS OF A CIRCLE IS A = πr²|")
print("+------------------------------------------+")

import numpy as np
radii = np.array([1,2,3])
print(np.pi * radii ** 2)

# ELEMENT WISE ARITHEMETIC
import numpy as np
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)
print()

# as a example we a are look... giving many result of student and look and find if anyone got any score == 100
import numpy as np
score = np.array([2,45,67,34,67,12,56,100])
print(score == 100)
print()

import numpy as np
score = np.array([23,4,5,44,4,56,67,62,54,67,67,78])
print(score <= 60)
print()

import numpy as np
score = np.array([12,3,5,56,67,78,78,32,34])
print(score >= 29)
print()
