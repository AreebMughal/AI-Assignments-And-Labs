from RetailItem import RetailItem

def main():
    item1 = RetailItem('Jacket', 12, 59.95)
    item2 = RetailItem('Designer Jeans', 40, 34.95)
    item3 = RetailItem('Shirt', 20, 24.95)
    
    print(f'Detail of Employee 1 is:\n{item1}\n')
    print(f'Detail of Employee 2 is:\n{item2}\n')
    print(f'Detail of Employee 3 is:\n{item3}\n')
    
main()