def printData():
    fields = []
    rows = []
    with open('students.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)        
        fields = next(csv_reader)
        for row in csv_reader:
            rows.append(row)
    
    print('=============================')
    print('ID\tName\t\tMarks')
    print('=============================')
    for row in rows:
        if (float(row[5]) > 80):
            name = row[1]+ ' '*(15-len(row[1])) if len(row[1]) <= 15 else row[1] # I used this to give proper spacing
            print(row[0] +'\t' + name +' '+ row[5])
    
    # data = pandas.read_csv(r'students.csv')
    # specific = pandas.DataFrame(data, columns=['ID', 'Name', 'Marks'])
    # print(specific)



printData()