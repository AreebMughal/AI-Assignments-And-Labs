



def take_input():
    name = input('Enter the name: ')
    age = ''
    while (type(age) is not int):
        try: 
            age = int(input('Enter your age: '))
        except Exception:
            print('Age can be only integer number')    
                        
    phone = input('Enter your phone number: ')
    qualification = input('Enter your qualification: ')
    
    return {'name': name, 'age': age, 'phone': phone, 'qualification': qualification}
    
    
def write_file(data):
    print(data)
    try: 
        file = open('lab_test.txt', 'w+')
        file.write("Name: {}, Age: {}, Phone Number: {}, Qualification: {}".format(data['name'], data['age'], data['phone'], data['qualification']))    
        file.close()
    except Exception as e:
        # print('Error in file opening/writing')
        print(e)
        

def main():
    
    data = take_input()
    
    write_file(data)
    
    
main()