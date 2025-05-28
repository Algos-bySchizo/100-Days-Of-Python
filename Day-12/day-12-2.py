""" Modifying the Global Scope """
#in this short block of code what we are trying to achieve is to increase the global variable's value inside a function!
enemies=3
def increase_enemies():
    #in order to get connected to the global variable we must call it by putting "global" before the "variable name"
    global enemies
    enemies+=1
    print(f"there are {enemies} no of enemies")
increase_enemies()
print(f"displaying enemies without using the function made for it! {enemies}")
# this is how you modify a global variable and use don't use it very often as it's not a very healthy approach and is more keen towards faliure
# what could we do instead is use return statements and modify the global statements in it!
enemies=0
def increase_enemies():
    # print(f"{enemies}")
    return enemies + 1
enemies=(increase_enemies())
print(f'{enemies}')
