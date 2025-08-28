import pandas

sq_data=pandas.read_csv('squirrel-data.csv')
# sq_color_data=sq_data['Primary Fur Color'].value_counts()
# sq_color_data.to_csv('color_counts.csv')

grey_squirrels=len(sq_data[sq_data["Primary Fur Color"]=='Gray'])
black_squirrels=len(sq_data[sq_data["Primary Fur Color"]=='Black'])
red_squirrels=len(sq_data[sq_data["Primary Fur Color"]=='Cinnamon'])
data_dic={
    'Color':['Black','Gray','Red'],
    'Count':[black_squirrels,grey_squirrels,red_squirrels]
    }
df=pandas.DataFrame(data_dic)
df.to_csv("new_csv_sqr.csv")
