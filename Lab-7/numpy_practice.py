
from ctypes import sizeof
import numpy as np
import sys

# arr = range(1000)
arr = [1,2,3,4,5,6,7,8,9,10]

# arr1 = np.arange(1000)

arr1 = np.array([1,2,3,4,5,6,7,8,9,10])

print(f'Array: {len(arr)}')
print(f'Numpy: {len(arr1)}')
print()
print(f'Size of Array: {sys.getsizeof(arr)}')

print(f'Size of Numpy: {arr1.itemsize}')

print(arr)
print(arr1)


print('---------------------------------')

# Create a 2-D array
b = np.array([[1, 2, 3], [4, 5, 6]])
# Prints "(2, 3)"
print(b.shape) # print dimension of the array => (row, col)

a = np.zeros((2, 2)) #create array of zeros
print(a)
a = np.ones((2, 2)) #create array of ones
print(a)

c = np.full((2, 2), 7) #creat 2-d array with all element 7
print(c)

d = np.eye(2) # create an indentity matric
print(d) 

# Create an array filled with random values
e = np.random.random((2, 2))
print(e)


print ('-------------------------------- Slicing --------------------------------')
# array([uperbound : lowerbound])  => uperbund is included while lowerbound is not included
# array([uperbound1 : lowerbound1], [uperbound2 : lowerbound2]) => 1st argument is for row and 2nd argument is for column

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(a)
b = a[:2, 1:3]
print(b)

a[2,2] = 0

print(a)

print('--------------------- Shaping -------------------------')

a = np.array([[1, 2], [3, 4], [5, 6]])

print(a.shape)

a = a.reshape(3, 4)

print(a)