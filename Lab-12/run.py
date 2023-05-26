
import csv
from numpy import character

characters = 'This is a paragraph'

def removeith(string, n):  
    first = string[:n]   
    last = string[n+1:]  
    return first + last

print(removeith(characters, 2))

def tupleCude():
    lis = [1, 2, 3]
    tup = []
    for li in lis: 
        cube = (li, li**3)
        tup.append(cube)
    tup = tuple(tup)
    print(tup)
    
tupleCude()

def write_csv_file():
    data = [
        ['Areeb', 1231, '181400149@gift.edu.pk'],
        ['Areeb', 1231, '181400149@gift.edu.pk'],
        ['Areeb', 1231, '181400149@gift.edu.pk'],
        ['Areeb', 1231, '181400149@gift.edu.pk']
    ]
    with open('./file.csv', 'w+', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(data)
        
print()
write_csv_file()

