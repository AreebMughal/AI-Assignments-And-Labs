

from ProductionWorker import ProductionWorker
employees = []

choice = 0 

while(choice != -1):
    name = input('Enter name: ')
    id = input('Enter Employee number: ')
    shift = int(input('Enter Shift number (1 for day and 2 for night): '))
    hour = float(input('Enter Hourly per rate: '))
    
    employees.append(ProductionWorker(name, id, shift, hour))
    
    choice = int(input('To add more press 1 and to exit press -1: '))

print('\nDetails of Employee are: ') 
for employee in employees:
    print(employee)
    print()