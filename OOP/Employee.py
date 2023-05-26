
from Person import Person 


class Employee(Person):
    def __init__(self, name, email, phone, age):
        super().__init__(name, email, phone)
        self.__age=age
        
    def getAge(self):
        return self.__age
    
    def __str__(self):
        return f'{super().__str__()}\nAge is: {self.getAge()}'