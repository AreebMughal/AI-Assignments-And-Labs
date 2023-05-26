
from RetailItem import RetailItem

class CashRegister:
    
    
    def __init__(self) -> None:
        self.__purchasedItems = []
        
    def purchase_item(self, retailItem):
        self.__purchasedItems.append(retailItem)
        
    def get_total(self):
        total = 0
        for item in self.__purchasedItems:
            total += item.get_price()
        return total
    
    def show_items(self):
        items = {}
        for item in self.__purchasedItems:
            if item not in items.keys():
                items[item] = 1
            else:
                items[item] = items[item] + 1
        
        print('---------------------------------------------------')
        print('\tYou bought these items')
        print('---------------------------------------------------')
        print('No.\tDescription \tUnits \tPrice \tQuantity')
        i = 0
        for item, quantity in items.items():
            print(str(i+1)  + '\t' + item.myPrint() + '\t' + str(quantity))
            i += 1
        print('---------------------------------------------------')
        print(f'Your total bill is: {self.get_total()}')
        self.clear()
                
    
    def clear(self):
        self.__purchasedItems = []
    

