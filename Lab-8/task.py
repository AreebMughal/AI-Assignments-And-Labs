
from statistics import mean
import sys
import traceback
import numpy
import pandas as pd

cust = pd.read_csv(r'./Cust_Purch_FakeData.csv')

# print(cust)

first5 = cust.iloc[numpy.arange(5)]
print(first5)

# info = cust.info()
print('Columns: ', len(cust.columns))
print('Entries: ', len(cust.values))

ages = cust['age']

print('Max Age: ', max(ages))
print('Min Age: ', min(ages))
print('Mean Age: ', mean(ages))

names = cust['first'].value_counts()

# for i in range(3):
#     print(names[i])

# 'prefix', 'first', 'last', 'email', 'gender', 'age', 'company',
#        'profession', 'phone', 'postal', 'province', 'cc_no', 'cc_exp',
#        'cc_type', 'price(CAD)', 'fav_color', 'ip', 'weekday', 'ampm', 'date'],
#       dtype='object')

print(names.head(3))
print()
print((cust['profession'] == 'Structural Engineer').value_counts())
print()
print(len(cust[(cust['profession'] == 'Structural Engineer') & (cust['gender'] == 'Male')]))



print()
# Index(['prefix', 'first', 'last', 'email', 'gender', 'age', 'company',
#        'profession', 'phone', 'postal', 'province', 'cc_no', 'cc_exp',
#        'cc_type', 'price(CAD)', 'fav_color', 'ip', 'weekday', 'ampm', 'date'],


print(cust[(cust['gender'] == 'Female') & (cust['profession'] == 'Structural Engineer') & (cust['province'] == 'AB')]['first'])


print()

print(min(cust['price(CAD)']))
print(max(cust['price(CAD)']))
print(numpy.average(cust['price(CAD)']))
    

print()

print(cust[(cust['price(CAD)'] == 0)][['first', 'price(CAD)']])

print()
print(cust[(cust['price(CAD)'] >= 100)][['first', 'price(CAD)']])

print()
print(len(cust[(cust['cc_no'] == 5020000000000230)][['first', 'cc_no', 'email']].values))