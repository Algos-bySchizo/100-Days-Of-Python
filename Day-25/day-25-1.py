import pandas

data=pandas.read_csv('weather_data.csv')
temprature=data['temp'].to_list()
print(temprature) #to get the hold of all the tempratures through out the week using pandas you just have to write data['temp']
