

speed = float(input('Enter the speed of the vehicle (mph): '))
while (speed <= 0):
    speed = float(input("You can't enter negative speed, Enter again: "))


time = int(input('Enter the hours: '))
while (time < 1):
    time = int(input("You can't enter less than 1 hour, Enter again: "))
    


def DisplayDistance(speed, time):
    print('Hour \t Distance Traveled')
    print('----------------------------------------')
    for hours in range(time):
        distance = (hours+1) * speed
        print(f'{hours+1} \t {distance}')
        


        
DisplayDistance(speed, time)