import pandas

""" Pandas way of finding the occurance of different color squirrel  """

sq_data=pandas.read_csv('squirrel-data.csv')
sq_color_data=sq_data['Primary Fur Color'].value_counts()
sq_color_data.to_csv('color_counts.csv')

""" Lenghty way of finding the occurance of different color squirrel  """

grey_squirrels=len(sq_data[sq_data["Primary Fur Color"]=='Gray'])
black_squirrels=len(sq_data[sq_data["Primary Fur Color"]=='Black'])
red_squirrels=len(sq_data[sq_data["Primary Fur Color"]=='Cinnamon'])
data_dic={
    'Color':['Black','Gray','Red'],
    'Count':[black_squirrels,grey_squirrels,red_squirrels]
    }
df=pandas.DataFrame(data_dic)
df.to_csv("new_csv_sqr.csv")

""" using set() function we can sort occurance of duplicate items inside a list """

sq_color_data=sq_data['Primary Fur Color'].to_list()
colors=set([c for c in sq_color_data if str(c)!="nan"])
print(colors)
