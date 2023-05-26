

from Car import Car
def main():

    used_car = Car('Audi', 2007, 12500, 21500.00, 4)
    # Display the car's data.
    print('Make:', used_car.get_make())
    print('Model:', used_car.get_model())
    print('Mileage:', used_car.get_mileage())
    print('Price:', used_car.get_price())
    print('Number of doors:', used_car.get_doors())
    
    print()
    
    print(used_car)

main() 