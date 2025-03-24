import random
alphab=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',':', 
           ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
nofalfa=int(input('Enter the number of alphabets you want'))
nofnum=int(input('Enter the number of numbers you want'))
nofsyms=int(input('Enter the number of symbols you want'))
password=[]
for alfa in range(nofalfa):
    password+=random.choice(alphab)
for num in range(nofnum):
    password+=random.choice(numbers)
for syms in range(nofsyms):
    password+=random.choice(symbols)
random.shuffle(password)
print(''.join(password))
