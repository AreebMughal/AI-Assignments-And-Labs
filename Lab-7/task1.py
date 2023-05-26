
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

# m = numpy.arange((11,27), dtype=int)
# m = m.reshape(4, 4)
# print(m[1: len(m)-1, 1 : len(m)-1])

print('\n---------------Task - 4 --------------')

myarray = numpy.array([[10, 11, 12, 13], [14, 15, 16, 17], [18, 19, 20, 21]])

print(f'Array is: \n{myarray}')
print(f'Shape of this is :{myarray.shape}' )
print(f'Rows: {myarray.shape[0]}, Columns: {myarray.shape[1]}')


print('\n---------------Task - 5 --------------')

myarray = numpy.array([[10, 11, 12, 13], [14, 15, 16, 17], [18, 19, 20, 21]])

print(f'2D Array is: \n{myarray}')

myarray = myarray.reshape(-1)
print(f'Array after converting into 1D: \n{myarray}')

print('\n---------------Task - 6 --------------')


myarray = numpy.arange(55, 90).reshape(5, 7)
print(f'5-by-7 matrix filled with values from 55 to 90: \n{myarray}')



