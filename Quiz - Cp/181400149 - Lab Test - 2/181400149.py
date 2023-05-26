

# -------------------------------------- Question 1 --------------------------------
print('-------------------------------------- Question 1 --------------------------------')
list = [5, 10, 15, 20, 25, 50, 20]

i = 0
for value in list:
    if (value == 20):
        list[i] = 200
        break
    i += 1   

print('List After Replacing: ')
for li in list:
    print(li)



# -------------------------------------- Question 2 --------------------------------
print('-------------------------------------- Question 2 --------------------------------')
import random

class Dice:
    
    def __init__(self):
        self.__dice = None
        
    def set_diceValue(self, value):
        self.__dice = value
        
    def get_diceValue(self):
        return self.__dice
    
    def roll_dice(self):
        self.set_diceValue(random.randint(1, 6))
        
        
player_1 = Dice()
player_2 = Dice()

player_1.roll_dice()
player_2.roll_dice()

if (player_1.get_diceValue() != None and player_2.get_diceValue() != None):
    if (player_1.get_diceValue() > player_2.get_diceValue()):
        print('Player 1 is winner')    
    elif (player_1.get_diceValue() < player_2.get_diceValue()):
        print('Player 2 in winner')
    else:
        print('Both player match is tie')
else: 
    print('You did not roll the dice')