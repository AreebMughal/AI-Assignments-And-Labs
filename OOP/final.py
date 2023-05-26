import pandas as pd
import numpy as np
names = ['Areeb', 'Shahana', 'Ali']

my_dic = {
    '149' : 'Areeb',
    '123' : 'Shahana',
    '213' : 'Ali'
}

keys = ['149', '123', '213']
my_series = pd.Series(data=names, index=keys)

print(my_series)

print(my_dic)

numbers = np.arange(20, 30)

print('Using Numpy')
print(pd.Series(data=numbers))

dic = {
    'x': 'Areeb',
    'y': 'Yashal',
    'z': 'Shahana'
}

print()
print('Using Dictionary')
newSeries = pd.Series(data=dic)
print()


print(newSeries['x'])

print(newSeries.tail(2))

print(dic.keys())

print(newSeries.axes)


# ------------------- Data Frames ------------

rows = 'r1 r2 r3 r4 r5 r6 r7 r8 r9 r10'.split()
columns = 'c1 c2 c3 c4 c5 c6 c7 c8 c9 c10'.split()

data = np.arange(100).reshape((10, 10))

my_data_frame = pd.DataFrame(data=data, index=rows, columns=columns)

print('\n\n', my_data_frame)

print(my_data_frame[['c2', 'c4', "c6"]])



my_data_frame.drop(['c5', 'c6'], axis=1, inplace=False)

print()
print(my_data_frame)


print()


print(my_data_frame.loc[['r2']])

print()


print(my_data_frame.iloc[[1, 2, 3, 0]])

print(my_data_frame.loc['r3', 'c6'])

print(my_data_frame.loc[['r2', 'r3'], ['c3', 'c4']])