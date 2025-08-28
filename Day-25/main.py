import csv
with open('weather_data.csv') as data:
    data=csv.reader(data)
    data=[data.strip() for data in data.readlines()]    
    print(data)
    # CSV library is a built-in python library that helps the programmers with CSV file handling and manipulation 
    tempratures=[] 
    for row in data:
        try:
            tempratures.append(int(row[1]))
        except:
            pass
        # print(row)
    print(tempratures)