print('***This is python practice file\n')

name = 'areeb mughal'
#Changing Case in a String
print(name.title()) 
print(name.upper()) 
print(name.lower()) 
print()

# Concantination
print('This', 'is', 'a concatenation' ) #it give space between different paramenters
print('This' + 'is')
print()

# Extra spacing in string
name = '  Areeb Mughal  '
print("'" + name.strip() + "'")
print("'" + name.lstrip() + "'")
print("'" + name.rstrip() + "'")

print('\n************************************ Math *************************************')

# Math 

print(2**4) # to take power use double **

print(5//3) #if we want to make ineger division then use double //
print(5/3) 
print()
number = [1, 3, 5, 6, 7]
print('Min:', min(number))
print('Max:', max(number))
print('Sum:', sum(number))

age = 20
# print('Happy ' + age + 'th Birthday') #it will give type error
str = 'Happy ' + str(age) + 'th Birthday' 
print(str)

print('\n************************************** Lists *************************************************')

# import this # The Zen of Python is a collection of 19 "guiding principles" for writing computer programs that influence the design of the Python programming language


# ************************************** Lists *************************************************

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1]) # -1 to access the last index of the list
print(bicycles[-2]) # -2 to access the second last index of the list and so on

print()

name = ['areeb', 'sharif', 'saher']
print(name)
name.append('rishna') # to add at the last of the list
name.insert(2, 'yashal') # to insert the element at specific index
name.append('waile')
print(name)

del name[0]
print(name)
print(name.pop()) # remove at the last of the list
print(name.pop(1)) # remove from the list at specific index
name.remove('sharif') # remove element by the value and it will delete the first occurrence in the list 
print(name)
print(type(name))
print(len(name))

st ='dajksfjk '
del st
del name # it will delete the any variable completely

# print(name, st)

mylist = [32, 8, 100, 323, 12] 
mylist.sort(reverse=True)      # sort the list permanently 
print(mylist)
mylist = ['zeeshan', 'bilal', 'ali']
mylist.sort()
print(mylist)

mylist = ['bilal', 23, 2, 'areeb'] # this list cannot be sort
print(mylist)

mylist = [32, 8, 100, 323, 12] 
print('Before', mylist) 
print('While Sorting', sorted(mylist))  #sort the list temporarily 
print('After', mylist)
print('While Sorting', sorted(mylist, reverse=True))

print()

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

print('\n-------------------------------> Loops <-------------------------------------')
# -------------------------------> Loops <-------------------------------------
for car in cars: 
    print(car)


print('\nLoop is closed ')
print(car)
print()

for i in range(1, 5):
    print(i)
    
squares = []
for i in range(1, 11):
    squares.append(i**2)

print('Squares:', squares)
    
# Making list with the range()

squares = [value**2 for value in range(1, 11)] # list comprehension 
print(squares)
print()

numbers = list(range(1, 6))
print(numbers)

odd = list(range(1, 11, 2))
li = list(range(1, 11, 3))
even = list(range(2, 11, 2))

print(odd)
print(even)
print(li)

print('\n--------------------------- Slicing the list --------------------------')

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[0:3])
print(players[-3:])
print(players[1:4])
print(players[:])
print()

for player in players[:3] :
    print(player)
    
print()

print('--------------------------- tupple -------------------------------')

dimensions = (200, 50)

print(dimensions)

mytuple = (1, 2, 4, 5, 'asr')
print(mytuple)
print(mytuple[0])

# mytuple[0] = 3


for element in mytuple:
    print(element)


# ================================ > Functions < ============================================

print('\n-------------------------------------- Funtions -----------------------------')

def myFunction():
    print("I'm in the function")

myFunction()

def functionWithParam(name):
    print('hello', name)
    
functionWithParam('Areeb')

def optionalParam(value = "Default"):
    print('Value is:', value)
    
    
optionalParam('Areeb')
optionalParam()

def multiply(num1, num2):
    return num1*num2

value = multiply(2, 4)
print(value)


def documentationFunc(num):
    """
        Hello, This is the documentation part of this function.
    """
    print(num**2)


documentationFunc
print(documentationFunc.__doc__)


def funcWithDoubleAssignment():
    x, y = 2, 5
    return x*5

print(f'Double Assignment Operator Function: {funcWithDoubleAssignment()}')

print()

def square(num):
    return num**2

sq = lambda num: num**2

print(square(2))
print(sq(2))

def trippler(num1):
    return lambda num2: num1*num2

multiply2 = trippler(2)
print(multiply2(5))

pr = lambda : "hello"

print(pr())

print('\n******************** Built in Functions ***********************')

print(max(3,4,1))
print(min(2,1,5))
print(max('a','A','b','Z', 'z'))

print()

print(round(4.764))
print(round(4.324))
print(round(4.764,1))
print(round(4.764,2))


print('---------------------------- Dictionary ----------------------')

