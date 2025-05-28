import os
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    while n2==0:
        print("invalid input denominator can't be 0!")
        n2=float(input('enter n2 again!'))
    return n1/n2
operations={
    '+':add, 
    '-':sub,
    '*':mul,
    '/':div,
}
def calculator():
    num1=float(input('Enter the first number: '))
    for operators in operations:
        print(operators) 
    end_program=False   
    while not end_program:
        select_operation=input('Pick the operation you want to perform: ')
        num2=float(input('Enter the second number: '))
        calculation_function=operations[select_operation]
        answer=calculation_function(num1,num2)
        print(f"{num1}{select_operation}{num2}={answer}")
        if input(f'Type "y" if you want to continue caluculation using previous answer or "n" to start all over again!')=='y':
            num1=answer
        else:
            end_program=True
            os.system('cls')
            calculator()
calculator()