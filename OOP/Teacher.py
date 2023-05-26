

from Person import Person 

class teacher(Person):
    def __init__(self, name, email, phone, degree):
        super().__init__(name, email, phone)
        self.__degree= degree
        
    def get_degree(self):
        return self.__degree
    
    def __str__(self):
        return f'{super().__str__()}\nDegree: {self.get_degree()}'