
class Person:
    def __init__(self, name, address, telephone):
        self.__name = name
        self.__address = address
        self.__telephone = telephone

    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_address(self, address):
        self.__address = address
    
    def get_address(self):
        return self.__address
    
    def set_telephone(self, telephone):
        self.__telephone = telephone
    
    def get_telephone(self):
        return self.__telephone
    
    def __str__(self):
        return f'Name: {self.get_name()} \nAddress: {self.get_address()} \nTelephone: {self.get_telephone()}'
