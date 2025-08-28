import pandas

""" Finding average of temprature """

data=pandas.read_csv('weather_data.csv')
temp_list=data['temp'].to_list()
avg=sum(temp_list)/len(temp_list)
print("{:.2f}".format(avg))

""" Finding average of temprature using the function of .mean() in Series data type in Pandas """

data=pandas.read_csv('weather_data.csv')
print(data['temp'].mean())

""" Finding the maximum temprature using the function .max() in Series data type in Pandas """

data=pandas.read_csv('weather_data.csv')
print(data['temp'].max())

""" Alternate approach "Attribute Approach" to get hold of a column in Pandas """

data=pandas.read_csv('weather_data.csv')
print(data['temp'])
# Alternate Way ⬇️
print(data.temp)

""" Getting hold of rows in Pandas """

data=pandas.read_csv('weather_data.csv')
# the code snippet below basically grabs the row where the temprature was at max, to break it down it should be readed as
# print data[accessing temprature column where temprature is at max using .max()]
print(data[data.temp==data.temp.max()])

""" Making objects and storing rows in them and treating them as we're treating the whole data """

monday=data[data.day=='Monday']
print(monday.condition)

""" Retrieving data from the object and coverting its temprature into fahrenheit """

monday=data[data.day=='Monday']
print(monday.temp)
print((monday.temp*9/5)+32)