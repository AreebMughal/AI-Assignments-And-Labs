
from Employee import Employee

class ProductionWorker(Employee):

    def __init__(self, name, id, shift_number, hourly_rate):
        super().__init__(name, id)
        self.__shift_number = shift_number
        self.__hourly_rate = hourly_rate    
        
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number
    
    def get_shift_number(self):
        if (self.__shift_number == 1):
            return 'Day'
        else:
            return 'Night'
    
    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate
    
    def get_hourly_rate(self):
        return self.__hourly_rate
    
    def __str__(self):
        return super().__str__() + f"\nShift: {self.get_shift_number()} \nHourly per rate: {self.get_hourly_rate()}"