with open('weather_data.csv') as data:
    data=[data.strip() for data in data.readlines()]
    print(data)