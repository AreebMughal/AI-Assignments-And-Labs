# *******************************************
# * FALL 2021 - Artificial Intelligence Lab *
# * MIDTERM PRACTICAL EXAM                  *
# *                                         *
# *******************************************
# *										    *
# * Computer.py implementation: 10          *
# *								            *
# *******************************************
# *                                         *
# * ID:                                     *
# * NAME:                                   *
# * SECTION:                                *
# *                                         *
# * INSTRUCTIONS:                           *
# * Complete the implementation of the      *
# * following code, indicated in comments.  *
# *******************************************

class Computer:

    # Complete the initializer with three private members
    # named as manufacturer, ram, serial_no                     [POINTS: 1]

    def __init__(self, manufacturer, ram, serial_no):
        self.manufacturer = manufacturer
        self.ram = ram
        self.serial_no = serial_no

    # write getters for all three members                       [POINTS: 1]
    def set_manufacturer(self):
        return self.manufacturer
    def set_ram(self):
        return self.ram
    def set_serial_no(self):
        return self.serial_no
    
    # write setters for all three members                       [POINTS: 1]
    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer
    
    def set_ram(self, ram):
        self.ram = ram

    def set_serial_no(self, serial_no):
        self.serial_no = serial_no
        
    # Complete implementation of str method with appropriate
    # message                                                   [POINTS: 1]

    def __str__(self):
        return f'Manufacturer: {self.manufacturer}, ram: {self.ram}, serial_no: {self.serial_no}'

# **************************************************************************
#
# Object Creation:
#
# Create three objects of above class with relevant information
# below this line                                               [POINTS: 2]

c1= Computer('Dell', 8, '12391223')
c2 = Computer('HP', 16, '23534523')
c3 = Computer('Dell', 32, '12345325')

# Create a list and add above three objects to the list         [POINTS: 2]

comps = [c1, c2, c3]

# write a loop to iterate through list and display all objects  [POINTS: 2]

for c in comps:
    print(c)



# **************************************************************************
# *                              END OF FILE                               *
# **************************************************************************