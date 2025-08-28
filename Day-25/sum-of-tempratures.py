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
