class RetailItem:
    
    def __init__(self, item_des, unit, price):
        self.__item_des = item_des
        self.__unit  = unit 
        self.__price = price
        
    def set_item_des(self, item_des):
        self.__item_des = item_des
    def set_unit(self, unit):
        self.__unit = unit
    def set_price(self, price):
        self.__price = price
    
    
    def get_item_des(self):
        return self.__item_des
    def get_unit(self):
        return self.__unit
    def get_price(self):
        return self.__price
    
    def __str__(self):
        return f'Description: {self.get_item_des()} \nUnits in Inventory: {self.get_unit()} \nPrice: {self.get_price()}'


