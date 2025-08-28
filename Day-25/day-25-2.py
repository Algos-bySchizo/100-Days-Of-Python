import pandas

data=pandas.read_csv('weather_data.csv')
print(type(data['temp']))
print(type(data))

""" to_dict() method in Pandas "DataFrame" to convert CSV data into dictionary """

data_dict=data.to_dict()
print(data_dict)

""" to_list() method in Pandas "Series" to convert a column's data into list """

temp_list=data['day'].to_list()
print(temp_list)

