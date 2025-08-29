import pandas

data=pandas.read_csv('50_states.csv')
states=data['state'].to_list()
# print(states)
guess="Ohio"
if guess in states:
    obj=data[data['state']==guess]
    print(int(obj.x.values[0]))