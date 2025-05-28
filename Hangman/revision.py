from Hangman.listofwords import listofwords
from Hangman.stages import stages
import random
import os
lives=6
chosen_word=random.choice(listofwords)
display=['_' for dog in range(len(chosen_word))]
print(','.join(display))
state_of_game=False
while not state_of_game:
    guess=input('Guess a letter!')
    if guess in display:
        print(f"you\'ve guessed {guess} already, guess another letter!")
        continue
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        os.system('cls')
        print(','.join(display))
        if guess==letter:
            display[position]=letter
            print('Congrats You\'ve guessed it right!')
            print(','.join(display))
    if guess not in chosen_word:
        lives-=1
        print('OOPS you\'ve guessed it wrong you lost a life!')
        print(stages[lives])
    if lives==0:
        state_of_game=True
        print('OOPS you ran out of lives :( GAME OVER')
if '_' not in display:
    state_of_game=True
    print("Congratulations You've Successfully Guessed the Right word!")