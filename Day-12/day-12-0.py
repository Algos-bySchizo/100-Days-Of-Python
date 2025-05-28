""" Local Scope """
#Local Scope can not be accessed everywhere they have to be used inside their scope!
def increase_enemies():
    enemies=2
    print(f"enemies inside the function {enemies}")
increase_enemies()
print(f"enemies outside the function {enemies}")

""" Global Scope """
#Global Scope can accessed anywhere they don't need to be called in their scope only!
enemies=10
def display_no_of_enemies():
    allies=5
    print(f"there are {enemies} no of enemies")
display_no_of_enemies()
print(f"displaying enemies without using the function made for it! {enemies}")

