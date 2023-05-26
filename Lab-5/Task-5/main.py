from Customer import Customer

customer1 = Customer('Areeb', 'College Road', '0123141242', 2131, True)
customer2 = Customer('Alina', 'Model Town', '7346958338', 1121, False)
customer3 = Customer('Sharif', 'Alam Chowk', '9809809098', 2340, True)

customers = [customer1, customer2, customer3]


print('\nDetails of Customers are: ')
for customer in customers:
    print(customer)
    print()


