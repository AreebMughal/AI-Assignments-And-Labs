from RetailItem import RetailItem
from CashRegister import CashRegister

cash = CashRegister()

item1 = RetailItem('Jacket', 12, 59.95)
item2 = RetailItem('Jeans', 40, 34.95)
item3 = RetailItem('Shirt', 20, 24.95)
item4 = RetailItem('Pents', 10, 10.50)
item5 = RetailItem('T-Shirt', 14, 30.34)

items = [item1, item2, item3, item4, item5]


def printItemsList(items):
    i = 0
    print('---------------- Menue ---------------')
    print('No.\tDescription \tUnits \tPrice')
    for item in items:
        print(str(i+1) + '\t' + item.myPrint())
        i += 1
    
    print('-1 to Exit')
    print('-2 to Check out')
        
        
choice = 0

while (choice != -1):
    printItemsList(items)
    choice = int(input('Enter your input: '))
    if (choice != -1 and choice != -2):
        cash.purchase_item(items[choice])
        items[choice].set_unit(items[choice].get_unit()-1)
    
    elif (choice == -2 or choice == -1):
        cash.show_items()
        choice = -1
  
    