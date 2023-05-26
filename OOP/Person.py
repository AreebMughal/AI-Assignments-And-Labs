
class Person:
    def __init__(self, name, email, phone):
        self.__name = name
        self.__email = email
        self.__phone = phone
        
    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    
    def get_phone(self):
        return self.__phone
    
    def __str__(self):
        return f'Name: {self.get_name()}\nEmail: {self.get_email()}\nPhone: {self.get_phone()}'