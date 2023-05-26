def MassAndWeight():

    weight = lambda mass: mass*39.8
    w = weight(float(input("Enter the mass: ")))


    print(f"Weight is: {w}")

    if w > 500:
        print(f"Weight is overloaded: {w}")
    elif w < 100:
        print(f"Weight is too light: {w}")
    else:
        print(f"Weight is average: {w}")


# MassAndWeight()

print('\n---------task-2')

import math 

def HotDogsCookoutCalculator():
    hotdog = 10
    hotdogbun = 8
    person = int(input("Enter the number of the people: "))
    hdog = int(input("Number of hot dog each person will be given: "))
    totaldogNeeded = person * hdog
    totalbunNeeded = person * hotdogbun
    
    hotdogrequired = math.ceil(totaldogNeeded/hotdog)
    hotdogbunrequired = math.ceil(totalbunNeeded/hotdogbun)
    print(f"The minimum number of packages of hot dogs required: {hotdogrequired}")
    print(f"The minimum number of packages of hot dogs bun required: {hotdogbunrequired}")
    print(f"The number of hot dogs that will be left over: {hotdogrequired*10 - totaldogNeeded}")
    print(f"The number of hot dogs bun that will be left over: {hotdogbunrequired*10 - totalbunNeeded}")
  
  
  
# HotDogsCookoutCalculator()

def MilesPerGallon():
    gallons=0
    totavg=0
    number=0
    print('dsf')
    while gallons != -1:
        gallons=float(input("Enter the number of galloans"))
        if (not(gallons < 0)):
            miles= float(input("Enter the number of miles"))
            avg=(miles/gallons)
            totavg=totavg+avg
            print("The avg for you vehical is :", avg)
            number=number+1
    print(totavg/number)

# MilesPerGallon()

def SoftwareSales():
    pkg = int(input("Enter the number of packages purchased: "))
    dis = 0.0
    if (pkg >= 10 and pkg <= 19):
        dis = (99.0*pkg) * .1
    elif (pkg >= 20 and pkg <= 49):
        dis = (99.0*pkg) * .2
    elif (pkg >= 50 and pkg <= 99):
        dis = (99.0*pkg) * .3
    elif (pkg >= 100):
        dis = (99.0*pkg) * .4
        
    print(f"Total Price: {99.0*pkg}")
    print(f"Discount: {dis}")
    print(f"Total amount of the purchase after the discount: {(99.0*pkg) - dis}")
    

SoftwareSales()