
class Employee:

    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def set_name(self, name):
        self.__name = name
    
    
    def get_name(self):
        return self.__name
    
    def set_id(self, id):
        self.__id = id
    
    def get_id(self):
        return self.__id
    
    def __str__(self):
        return f'Name: {self.get_name()} \nID: {self.get_id()}'
