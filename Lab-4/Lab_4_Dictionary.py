
def practice():
    myDic = {'areeb' : '181400149', 'sharif': '18140099', 'saher': '18140132', 'rishna': '181400138', 'yashal': '181400157'}

    print(myDic.get('sharif'))
    print(myDic.get(0)) # will return none
    print(myDic.get('saher', 'Key Not Found'))
    print(myDic.get('salman', 'Key Not Found'))


    test_scores = { 'Kayla' : [88, 92, 100],
    'Luis' : [95, 74, 81],
    'Sophie' : [72, 88, 91],
    'Ethan' : [70, 75, 78] }

    for member in test_scores:
        print(f'{member}: ')
        for scores in test_scores[member]:
            print(f"{scores}")
            
        print('----------------------')
        
        
    for key, value in test_scores.items():
        print(f'Key: {key}')
        print(f'Value: {value}')
    
    

import random
def CapitalQuiz():

    capital_dic={
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Neveda': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakoda': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'  
}
    
    
    states = list(capital_dic.keys())
    
    correct = 0
    wrong = 0
    rand = random.randint(0, len(states))
    mychar = '0'
    while (mychar != '-1'):
        mychar = input(f'What is the Capital of State "{states[rand]}" or enter -1 to exit: ')
        
        if (mychar != '-1' and mychar == capital_dic[states[rand]]):
            correct += 1
        elif(mychar != '-1'):
            wrong += 1
            
        rand = random.randint(0, len(states))
    
    print(f'You tell {correct} Correct and {wrong} Wrong')

# CapitalQuiz()    

def CourseInformation():
    room = { 'CS101': '3004',
                'CS102': '4501',
                'CS103': '6755',
                'NT110': '1244',
                'CM241': '1411',
            }
    
    instructor = { 'CS101': 'Haynes',
                'CS102': 'Alvarado',
                'CS103': 'Rich',
                'NT110': 'Burke',
                'CM241': 'Lee',
            }
    
    meeting_time = { 'CS101': '8:00 a.m.',
                'CS102': '9:00 a.m.',
                'CS103': '10:00 a.m.',
                'NT110': '11:00 a.m.',
                'CM241': '1:00 p.m.',
            }
    
    print('-------------------------------')
    print('Courses \t Rooms')
    print('-------------------------------')
    
    for key, value in room.items():
        print(f'{key} \t\t {value}')
        
    print('-------------------------------')
    print()
    
    print('-------------------------------')
    print('Courses \t Instructor')
    print('-------------------------------')
    
    for key, value in instructor.items():
        print(f'{key} \t\t {value}')
        
    print('-------------------------------')
    print()
    
    print('-------------------------------')
    print('Courses \t Meeting Timing')
    print('-------------------------------')
    
    for key, value in meeting_time.items():
        print(f'{key} \t\t {value}')
        
    print('-------------------------------')
    
# CourseInformation()
from pathlib import Path


def Encrpyt():
    encryption_library = {'A':'!','B':'@','C':'#','D':'$','E':'%','F':'^','G':'&','H':'*','I':'(',
                      'J':')','K':'-','L':'_','M':'+','N':'=','O':'`','P':'~','Q':'{','R':'[',
                      'S':'}','T':']','U':':','V':';','W':'"','X':'<','Y':'>','Z':'0','a':'1',
                      'b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'a',
                      'k':'b','l':'c','m':'d','n':'e','o':'f','p':'g','q':'h','r':'i','s':'j',
                      't':'k','u':'l','v':'m','w':'n','x':'o','y':'p','z':'q'}
    
    file = open('file.txt')
    # fle = Path('data.txt')
    # fle.touch(exist_ok=True)
    # f = open(fle, 'w')
    f = open('data.txt', 'r+')
   
    def getkeyFromValue(dic, val):
        key = [key for key, value in dic.items() if value == val]
        if key:
            return key[0]
        else:
            return val
    
    def encrypt():
        for character in file.read():
            if (character in encryption_library.keys()):
                f.write(encryption_library[character])
            else:
                f.write(character)
                
        
    def decrypt():
        file2 = open('decrypt.txt', 'w')
        for character in f.read():
            key = getkeyFromValue(encryption_library, character)
            file2.write(key)
        
    ch = int(input('Press:- \n1 to Encrypt \n2 to Decrypt: '))
    if (ch == 1):
        encrypt()
    elif (ch == 2):
        decrypt()
    
        
    # print(file.read(1))
     
Encrpyt()

    # item_name, quantity, price and total arguments    
    
def ShoppingCart():
    items = {}
    total = 0
    
    def add_item(item_name, quantity, price, total):
        total += (quantity * price)
        items[item_name] = [quantity, price]
        return total
    
    def remove_item(item_name, quantity, total):
        if (item_name in items.keys()):
            price = items[item_name][1]
            if (items[item_name][0] >= quantity):
                total -= (quantity * price)
                new_quantity = items[item_name][0] - quantity
                items[item_name][0] = new_quantity
                if (new_quantity == 0):
                    del items[item_name]
            else:
                print('You Enter the Quantity that is greater than Cart\'s Quantity!')
        else:
            print('The item you entered in not in Shopping Cart')

        return total
            
    def checkout():
        cash = float(input(f'Your total bill is {total} \nEnter the cash: '))
        if (cash >= total):
            print(f'You bill is paid sucessfully paid and your remaining is {cash-total}')
        else:
            print('Cash paid not enough')
        
    ch = 1
    while (ch != 0):
        ch = int(input('****** Press ****** \n"1" to Add Item.\n"2" to Delete Item\n"3" to Checkout\n"0" to Exit the program: '))
        print() 
        if (ch == 1):
            item_name = input('Enter the name of the Item: ')
            quantity = int(input('Enter the quantity: '))
            price = float(input('Enter the price per item: '))
            total = add_item(item_name, quantity, price, total)
        elif (ch == 2):
            item_name = input('Enter the name of the Item: ')
            quantity = int(input('Enter the quantity: '))
            total = remove_item(item_name, quantity, total)
        elif (ch == 3):
            checkout()
        
    # print(items)
    # print(total)

    
# ShoppingCart()