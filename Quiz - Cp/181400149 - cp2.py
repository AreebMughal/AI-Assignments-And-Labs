# INSTRUCTIONS

# Class Participation 03

# 1. File name should be "Your_ID.py" e.g "18802585.py".
# 2. You don't need to create a new file. Edit this file and add your answer.
# 3. Finally, submit this file with your answers.
# 4. If you've any additional files like "story.txt" / "student.csv", don't submit them.
# 5. Only SUBMIT this "Your_ID.py" file with your answers.
# 6. Don't edit or remove any line or comment.


# Exercise-01
# Create an array of table 02 unig Numpy Array and then Iterate it.
# 
# 
import numpy
print('\n---------------Task - 1 --------------')

size = 10
table = 2
table_array = numpy.arange(table, (size*table + table), table)
# print(table_array)
print('Table:')
i = 1
for val in table_array:
    print(f'{table} * {i} = {val}')
    i += 1
    
# 
# 
# Exercise-02
# Create 8-by-8 matrix and fill it with a pattern of checkerboard like
# 0 1 0
# 1 0 1
# 0 1 0
# 
# 
print('\n---------------Task - 2 --------------')

checkboard = numpy.empty(64, dtype=int).reshape(8,8)
for i in range(8):
    for j in range(8):
        sum = i+j
        if (sum%2 == 0):
            checkboard[i, j] = sum - sum
        else:
            checkboard[i, j] = sum - (sum - 1)

print(f'Checkboard: \n{checkboard}')
# 
# 
# Exercise-03
# Create 10-by-10 matrix, in which the elements on the borders will be equal to 1, and inside 0.
# 
# 
print('\n---------------Task - 3 --------------')

            # ==> Method No. 1
oneBorders = numpy.zeros((10, 10), dtype=int)
oneBorders[0:1] = 1
oneBorders[:, 0:1] = 1
oneBorders[len(oneBorders)-1:] = 1
oneBorders[:, len(oneBorders)-1] = 1

            # ==> Method No. 2
# oneBorders = numpy.ones((10,10), dtype=int)
# oneBorders[1: len(oneBorders)-1, 1 : len(oneBorders)-1] = 0
print(f'Matrix with all borders 1 and inside 0: \n{oneBorders}')
# 
# 
# Exercise-04
# Create a given matrix first then find the number of rows and columns.
# [[10 11 12 13]
# [14 15 16 17]
# [18 19 20 21]]
# 
# 
print('\n---------------Task - 4 --------------')

myarray = numpy.array([[10, 11, 12, 13], [14, 15, 16, 17], [18, 19, 20, 21]])

print(f'Array is: \n{myarray}')
print(f'Shape of this is :{myarray.shape}' )
print(f'Rows: {myarray.shape[0]}, Columns: {myarray.shape[1]}')
# 
# 
# Exercise-05
# Reshape above 2-D array to one dimensional array
# 
# 
print('\n---------------Task - 5 --------------')

myarray = numpy.array([[10, 11, 12, 13], [14, 15, 16, 17], [18, 19, 20, 21]])

print(f'2D Array is: \n{myarray}')

myarray = myarray.reshape(-1)
print(f'Array after converting into 1D Array: \n{myarray}')
# 
# 
# Exercise-06
# Create a 5-by-7 matrix filled with values from 55 to 90
# 
# 
print('\n---------------Task - 6 --------------')


myarray = numpy.arange(55, 90).reshape(5, 7)
print(f'5-by-7 matrix filled with values from 55 to 90: \n{myarray}')

# 
# 
########################END########################