import csv
import pandas
# with open('weather_data.csv') as data:
#     data=csv.reader(data)
#     # CSV library is a built-in python library that helps the programmers with CSV file handling and manipulation 
#     tempratures=[] 
#     for row in data:
#         try:
#             tempratures.append(int(row[1]))
#         except:
#             pass
#         # print(row)
#     print(tempratures)
    # data=[data.strip() for data in data.readlines()]    
    # print(data)
data=pandas.read_csv('weather_data.csv')
print(data['temp']) #to get the hold of all the tempratures through out the week using pandas you just have to write data['temp']