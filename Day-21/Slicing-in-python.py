""" Slicing a list in python """

list=['a','b','c','d','e']
print(list[2:4])

""" Slicing from an index to the end """

list=['a','b','c','d','e']
print(list[2:])

""" Slicing from the start to a specific index """

list=['a','b','c','d','e']
print(list[:4])

""" Increment by a number while slicing between a range of items in a list """

list=['a','b','c','d','e','f','g','h']
print(list[1:6:2])

""" Increment by 2 while slicing items from the start to the end  in a list """

list=['a','b','c','d','e','f','g','h']
print(list[::2])

""" reverse slicing items from the end to the start in a list """

list=['a','b','c','d','e','f','g','h']
print(list[::-1])

""" reverse incremental slicing items from the end to the start in a list """

list=['a','b','c','d','e','f','g','h']
print(list[::-2])
