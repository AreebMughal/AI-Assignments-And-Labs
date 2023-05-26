

student = {}

ch = 0

while (ch != -1):
    roll = input('Enter the roll no: ')
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    
    student[roll] = [name, email]
    
    ch = int(input('If you want to add more press 1 and to exist press -1: '))
    print()
    
    find = '1'
while (find != '-1'):
    find = input('Enter the roll number you want to search or to exit press -1: ')
    if (find in student.keys()):
        print(f'Name: {student[find][0]}\nEmail: {student[find][1]}')
    elif(find != '-1'):
        print('This roll no is not in the list')