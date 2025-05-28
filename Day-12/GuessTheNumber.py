import os
import random
def guessthenumber():
    def hard(number):
        lives=5
        while lives>0:
            guess=int(input('Guess the number I\'m thinking of: '))
            if guess==number:
                print("you won!")
                return
            elif guess > number:
                lives -= 1
                print(f"Too high. You're down to {lives} lives.")
            else:
                lives -= 1
                print(f"Too low. You're down to {lives} lives.")
        print('You lost the game!')
    def easy(number):
            lives=10
            while lives>0:
                guess=int(input('Guess the number I\'m thinking of: '))
                if guess==number:
                    print("you won!")
                    return
                elif guess > number:
                    lives -= 1
                    print(f"Too high. \nYou're down to {lives} lives.")
                else:
                    lives -= 1
                    print(f"Too low. \nYou're down to {lives} lives.")
            print('You lost the game!')     
    print('Welcome to the Guess the number and win!')
    number=random.randint(1,100)
    print('I\'m thinking of a number between 1-100')
    if input("choose difficulty! type 'easy' or 'hard': ")=='easy':
        easy(number)    
    else:
        hard(number)
    if input('would you like to go again! (Y/N)').lower()=='y':
        os.system('cls')
        guessthenumber()
    else:
         print('thanks for playing!')
guessthenumber()    