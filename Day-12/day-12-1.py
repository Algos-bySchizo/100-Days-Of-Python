""" Python Doesn't have a Block Scope """

game_level=3
enemies=['skeletalman','potionman','steeleman',]
if game_level<5:
    display_enemy=enemies[0]
    #the Print staatement below works just fine concluding the fact that there is no block scope in Python 🐍
print(display_enemy)

""" Trying to print a Variable from a function outside of it this will throw an error """

game_level=3
def display_enemy():
    enemies=['skeletalman','potionman','steeleman',]
    if game_level<5:
        display_enemys=enemies[0]
        #the Print staatement below works just fine concluding the fact that there is no block scope in Python 🐍
    print(display_enemys)
print(display_enemys)
