# from Employee import Employee
#
# emp1 = Employee('Susan Meyers', 47899, 'Accounting', 'Vice President')
# emp2 = Employee('Mark Jones', 39119, 'IT', 'Programmer')
# emp3 = Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer')
#
# print(f'Detail of Employee 1 is:\n{emp1}\n')
# print(f'Detail of Employee 2 is:\n{emp2}\n')
# print(f'Detail of Employee 3 is:\n{emp3}\n')


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
    with open('students.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(fields)
        for s in std:
            csv_writer.writerow(s)


# creatFile_insertData()

def printData():
    fields = []
    rows = []
    with open('students.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        fields = next(csv_reader)
        for row in csv_reader:
            rows.append(row)

    # print(fields)
    # print(rows)
    # print("Field names are: " + ", ".join(field for field in fields))

    for row in rows:
        print(row)

    data = pandas.read_csv(r'students.csv')
    specific = pandas.DataFrame(data, columns=['ID', 'Name', 'Marks'])
    print(specific)


printData()
