

def pricatice():
    i = 1
    while i < 5:
        print('The value of i is: ', i)
        i += 1
    else:
        print('Exit loop')
    
    
def BudgetAnalysis():
    bugdet = float(input("Enter the amount of budgeted for a month: "))
    total = 0
    exp = 0
    while (exp != -1):
        i = 1        
        exp = float(input(f"Enter your expense# {i} or -1 to exit the loop: "))
        total += exp
        i += 1
    if (total > bugdet):
        print('Your expense is over the budget')
    else:
        print('Your expense is below the budget')
    
# BudgetAnalysis()


def AverageRainfall():
    years = int(input("Enter the number of years: "))
    total_month = 0
    total_inches = 0
    for year in range(years):
        for month in range(12):
            inch = float(input(f"Enter inches of rainfall for month {month+1}: "))
            total_inches += inch
            total_month += 1
    
    print(f"Total number of months is {total_month}")
    print(f"Total rainfall inches is {total_inches}")
    print(f"Average rainfall per month for the entire period is {total_inches/total_month}")
    
# AverageRainfall()

def PenniesforPay():
    days = int(input("Enter the days your worked: "))
    penny = 0
    print(f'-------------------Salary table-------------------')
    print(f'||      Days         ||       Salary            ||')
    print(f'--------------------------------------------------')
    
    for day in range(days):
        i = 1
        penny += i
        print(f'||      Day{i}         ||       {penny} Pennies        ||')
    else: 
        print(f'--------------------------------------------------')
        
    print(f'\nTotal pay is {penny/100} Dollars')
    
# PenniesforPay()

def OceanLevel():
    millimetersPY = 1.6
    years = 25
    millimeter = 0
    
    for year in range(years):
        millimeter += 1.6
        print(f"Ocean's level is rising for year {year+1}: {millimeter}")
        
# OceanLevel()
import random
def GuesstheNumber():
    choice = 1
    while(choice == 1):
        randon_number = random.randint(1, 1000)
        num = 0
        while(num != randon_number):
            num = int(input('Guess my number between 1 and 1000 with the fewest guesses: '))
            if (num == randon_number):
                print("Congratulations. You guessed the number!")
                choice = input(int('If you want to play more press 1 otherwise press -1'))
            elif(num > randon_number):
                print("Too high. Try again.")
            else:
                print("Too low. Try again.")
            
    
# GuesstheNumber()



def Population():
    organism = int(input(f"Starting number of organisms: "))
    percentage = int(input(f"Average daily increase in percentage: "))
    days = int(input(f"Number of days to multiply: "))    
    print('\n Day Approximate     Population')
    print('----------------------------------')
    sum = organism
    for day in range(days):
        print(f'  {day+1} \t {organism}')
        perc = organism*.3
        sum = organism + perc
        organism = sum
        
        
Population()