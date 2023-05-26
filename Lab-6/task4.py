
import random
from faker import Faker
import csv
import pandas
fields = ['ID', 'Name', 'Dept', 'CGPA', 'Semester', 'Marks']

fake = Faker()

std = []
for i in range(50):    
    id = random.randint(100, 999)
    name = fake.first_name()
    dept = fake.last_name() + ' Dpt'
    cgpa = round(random.uniform(1.00, 3.99), 2)
    semester = random.randint(1, 7)
    marks = random.randint(10, 100)
    std.append([id, name, dept, cgpa, semester, marks])

    
def creatFile_insertData():
    with open('students.csv', 'w+', newline='') as csv_file: # I used 'w+' so that if I want to override the previous file.
        csv_writer = csv.writer(csv_file)
        
        csv_writer.writerow(fields)
        for s in std:
            csv_writer.writerow(s)
    

def printData():
    fields = []
    rows = []
    with open('students.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)        
        fields = next(csv_reader)
        for row in csv_reader:
            rows.append(row)
    
    print('=============================')
    print('ID\tName\t\tMarks')
    print('=============================')
    for row in rows:
        if (float(row[5]) > 80):
            name = row[1]+ ' '*(15-len(row[1])) if len(row[1]) <= 15 else row[1] # I used this to give proper spacing
            print(row[0] +'\t' + name +' '+ row[5])
    
    # data = pandas.read_csv(r'students.csv')
    # specific = pandas.DataFrame(data, columns=['ID', 'Name', 'Marks'])
    # print(specific)


creatFile_insertData()
printData()


