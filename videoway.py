import random
import os
from stages import stages
from listofwords import listofwords
lives=6
chosenword=random.choice(listofwords)
# print(chosenword)
display=['_' for dog in chosenword]
print(','.join(display))
endofgame= False
while not endofgame:
    guess=input("Guess a letter!\t").lower()
    os.system('cls')
    if guess in display:
        print(f'you\'ve already guessed {guess} guess again!')
        continue
    for position in range(len(chosenword)):
        letter=chosenword[position]
        if letter==guess:
            display[position]=letter
            print(f'you\'ve guessed {letter} correctly')
    print(','.join(display),'\n')
    if guess not in chosenword:
        lives-=1
        print(f'OOPS {guess} is not in word!')
        if lives==0:
            endofgame=True
            print('you ran out of lives, you\'ve lost.') 
    if "_" not in display:
        endofgame=True 
        print('you\'ve guessed it right, you won!')
    print(stages[lives])