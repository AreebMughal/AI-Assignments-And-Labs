
import pandas as pd

cust = pd.read_csv(r'./Cust_Purch_FakeData.csv')


print('\n' + '-'*50 + '\n')


# Part - 1
maestro = cust[(cust['cc_type'] == 'Maestro')]
print('No. of people who use Maestro Card: ', len(maestro.values))


# Part - 2
print('\n' + '-'*50 + '\n')
print('The Customers who spent 100 or more CAD are: ')
mostspent = cust[(cust['price(CAD)'] >= 100)]
print(mostspent)


print('\n ==> Only name of them: ')
names = (mostspent['first'] + ' ' + mostspent['last'])

i = 1
for n in names:
    print(f'{i}) {n}')
    i += 1
    

# Part 3

print('\n' + '-'*50 + '\n')

names = cust['first'].value_counts()
names = names.head(3)

print('First 3 Most Common Names are: ')
i = 1
for name in names.axes[0]:
    print(f'{i}) {name}')
    i += 1
    
