""" Prime Number Excercise Day-08 """
import math
n=int(input('enter a number'))
def prime_number(number):
    no_of_numbers=0
    for evry_number in range(1,number+1):
        if number%evry_number==0:
            no_of_numbers+=1
    if no_of_numbers==2:
        print(f'{number} is a Prime number')
    else:
        print(f'{number} is not a prime number')
prime_number(number=n)