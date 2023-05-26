# *******************************************
# * FALL 2021 - Artificial Intelligence Lab *
# * MIDTERM PRACTICAL EXAM                  *
# *                                         *
# *******************************************
# *    *
# * Person.py implementation: 10            *
# *            *
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

class Person:


    # Complete the initializer with three private members
    # named as name, gender, birth_year                         [POINTS: 1]

    def __init__(self, name, gender, birth_year):
        self.name = name
        self.gender = gender
        self.birth_year = birth_year

    # write getters for all three members                       [POINTS: 1]
    def set_name(self):
        return self.name
    def set_gender(self):
        return self.gender
    def set_birth_year(self):
        return self.birth_year
    
    # write setters for all three members                       [POINTS: 1]
    def set_name(self, name):
        self.name = name
    
    def set_gender(self, gender):
        self.gender = gender

    def set_birth_year(self, birth_year):
        self.birth_year = birth_year
        
    # Complete implementation of str method with appropriate
    # message                                                   [POINTS: 1]

    def __str__(self):
        return f'Name: {self.name}, Gender: {self.gender}, Year: {self.birth_year}'


# **************************************************************************
#
# Object Creation:
#
# Create three objects of above class with relevant information
# below this line                                               [POINTS: 2]


p1= Person('Hafsa', 'Female', '1999')
p2 = Person('Anam', 'Female', '2001')
p3 = Person('Usama', 'Male', '1997')

# Create a list and add above three objects to the list         [POINTS: 2]

persons = [p1, p2, p3]

# write a loop to iterate through list and display all objects  [POINTS: 2]




# **************************************************************************
# *                              END OF FILE                               *
# **************************************************************************