from resources import resources, menu, profit

def report():
    print(f""" 
Water = {resources['water']} ML
Coffee = {resources['coffee']} MG
Milk = {resources['milk']} ML
Profit = ${profit}
""")
    return

is_on=True
while is_on:
    choice=input('what would you like to have to drink? (Espresso/Latte/Cappuccino?) : ').lower()
    is_on=choice!='off'
    if choice=='report':
        report()
    else:
        drink=menu.get(choice)
        if drink:
            continue
        else:
            print('')
