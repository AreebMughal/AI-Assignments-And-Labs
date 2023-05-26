

from Person import Person

class Customer(Person):
    
    def __init__(self, name, address, telephone, cus_number, mail_flag):
        super().__init__(name, address, telephone)
        self.__cus_number = cus_number
        self.__mail_flag = mail_flag
        
    
    def set_cus_number(self, cus_number):
        self.__cus_number = cus_number
    
    def get_cus_number(self):
        return self.__cus_number
    
    def set_mail_flag(self, mail_flag):
        self.__mail_flag = mail_flag
    
    def get_mail_flag(self):
        return self.__mail_flag
    
    def __str__(self):
        return super().__str__() + f"\nCustomer Number: {self.get_cus_number()} \nCustomer wants to mail: {self.get_mail_flag()}"