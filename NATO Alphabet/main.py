import pandas
dict=pandas.read_csv('natoalfa.csv')
pho_dict={row.letter:row.code for (index,row) in dict.iterrows()}
game_is_on=True
while game_is_on:
    user_input=input('enter any word!\t').upper()
    if user_input=='EXIT':
        game_is_on=False
        break
    else:
        pass
    output_list=[pho_dict[letter] for letter in user_input]
    print(output_list)
