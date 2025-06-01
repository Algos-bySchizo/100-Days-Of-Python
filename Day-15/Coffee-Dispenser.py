from resources import resources, menu, profit
def report():
    print(f""" 
Water = {resources['water']} ML
Coffee = {resources['coffee']} MG
Milk = {resources['milk']} ML
Profit = ${profit}
""")
    return
def process_money():
    """ Returns the total calculated from the coins inserted! """
    print('Please insert the coins!')
    total=int(input('How many quaters?'))*0.25
    total+=int(input('How many dimes?'))*0.1
    total+=int(input('How many nickels?'))*0.05
    total+=int(input('How many pennies?'))*0.01
    return total
def is_resource_sufficient(order_ingredients):
    """ Returns True when the resources are enough to process the order and False when not! """
    for ingredients in order_ingredients:
        if order_ingredients[ingredients]>resources[ingredients]:
            print(f"you do not have enough {ingredients}")
            return False
    return True
def is_transaction_successful(money_received,drink_cost):
    if money_received>drink_cost:
        change=round(money_received-drink_cost,2)
        print(f'here\'s your change {change}')
        global profit 
        profit+=drink_cost
        return True
    else:
        print('Sorry that\'s not enough money to proces the order, here\'s your refund!')
        return False    

def make_coffee(drink_name,order_ingredients):
    for ingredients in order_ingredients:
        resources[ingredients]-=order_ingredients[ingredients]
    print(f'Here\'s your {drink_name}, Thanks!')

is_on=True
while is_on:
    choice=input('what would you like to have to drink? (Espresso/Latte/Cappuccino?) : ').lower()
    # is_on=choice!='off'
    if choice=='report':
        report()    
    elif choice=='off':
        is_on=False
    else:
        drink=menu.get(choice)
        if is_resource_sufficient(drink['ingredients']):
            payment=process_money()
            if is_transaction_successful(payment,drink['cost'])==True:
                make_coffee(choice,drink['ingredients'])