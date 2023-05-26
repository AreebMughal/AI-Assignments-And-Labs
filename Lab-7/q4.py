
import pandas
data = pandas.read_csv(r'car_sales.csv')
specific = pandas.DataFrame(data)
list = list(specific.values)

for row in list: 
    if (int(row[2]) > 40 and int(row[6]) > 4):
        print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])

