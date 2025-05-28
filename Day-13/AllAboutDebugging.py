""" De-bugging """
def my_function():
    #The line below wasn't printing the print staement as the i never reached the index 20, 0-19=20 in binary index!
    # for i in range(1,20):
    for i in range(1,21):
        if i==20:
            print('you got it!')
my_function()

""" Reproducing The Bug """
import random
dice_sides=["1","2","3","4","5","6"]
#the line below was causing an index error
# dice_num=random.randint(1,6)
dice_num=random.randint(1,5)
# # print(dice_sides[dice_num])

""" Evaluate Each Line! """

year=int(input('Enter your birth year!'))
#The line below was throwing a operator logic bug where 1994 wasn't getting checked when the code ran! 
#if year>=1980 and year<1994:
if year>=1980 and year<=1994:
    print("you're a millenial")
elif year>1994:
    print('you\'re a gen-z')

""" Fixing Errors and watching Red Underlines closely! """
#The line below was causing the program to throw aa type error as it was taking the inout in string and was checking it in an int manner!
# age=input('Enter your age!')
age=int(input('Enter your age!'))
if age>18:
    # The Below has a small but impactful error as its an F-string!
    # print('you\'re of legal age to drive at {age}')
    print(f'you\'re of legal age to drive at {age}')

""" Print Statements are your Friend! """

pages=0
words_per_page=0
pages=int(input('enter the numbe of pages'))
# the line below was causing the bug in the code as it contains an equal to operator rather than an assignment one!
# words_per_page==int(input('enter the numbe of words per page'))
words_per_page==int(input('enter the numbe of words per page'))
total_words=pages*words_per_page
print(f"total number of words in the book are {total_words}")

""" Bringing Out the Big Guns a Debugger """
def mutate(a_list):
    b_list=[]
    for i in a_list:
        n=i*2
        print(n)
        b_list.append(n)
    # The line below was causing the issue as when the loop ran through all the items in the list it only appended last item rather than appening every item in the list
    # b_list.append(n)
    print(b_list)

mutate([1,2,3,4,5,6])

""" Even Odd Debugging """

number=int(input('Enter the number you want to check if is even or odd!: '))
# if number % 5 =0: (This was the line causing the bug as it's an assigment operator rather than  an equals to operator!)
if number % 5 ==0:
    print('is even')
else:
    print('is odd')

""" Leap-Year Debugging """

# year=input('enter the year you want to check if is leap or not!') (In the begining we didn't specify the data type we need which was int)
year=int(input('enter the year you want to check if is leap or not!'))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("is leap year!")
        else:
            print('is not leap!')
    else:
        print('is not leap!')
else:
    print('is not leap!')

""" Fizz-Buzz Debugging """

for number in range(1,101):
    # if number%3==0 or number%5==0: (here we have a small logical error in the conditioning as we can see we used 'or' instead of 'and')
    if number%3==0 and number%5==0:
        print('FizzBuzz')
    elif number%5==0:
        print('buzz')
    elif number%3==0:
        print('fizz')
    else:
        print(number)
