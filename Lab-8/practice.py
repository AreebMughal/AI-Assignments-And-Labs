#   Series - DataFrame

import pandas
mydic = {11: 'Integer', 'Areeb': 1222, 223.21: 'Double'} 

print(mydic)


keys = ['x', 'y', 2]
values = [1, 2, 3]

s1 = pandas.Series(data=values)

print(s1)

s2 = pandas.Series(data=values, index=keys)

print(s2)


