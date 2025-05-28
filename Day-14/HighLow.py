import random
import os
from artist_data import artists_data
from art import logo, vs
def highlow():
    def get_artist(exclude=None):
        celeb=random.choice(list(artists_data.items()))
        while exclude and celeb[0] == exclude[0]:
            celeb = random.choice(list(artists_data.items()))
        return celeb
    def format_print(c1,c2): 
        return f'''
    Option A = {c1[0]}
    Search Count = {c1[1]}
    {vs}
    Option B = {c2[0]}
    Search Count = ???'''
    def compare():
        print(logo)
        score=0
        celeb1=get_artist()
        while True:
            celeb2=get_artist(exclude=celeb1)
            print(format_print(celeb1,celeb2))  
            guess=input(f'\nChoose in between A and B, which has got more no of searches: ').strip().lower()
            if guess not in ['a','b']:
                print('Enter a valid character!')
                continue
            if (guess=='a' and celeb1[1]>celeb2[1]) or (guess=='b' and celeb2[1]>celeb1[1]):
                os.system('cls')    
                score+=1
                print(f'correct your score is now {score}')
                celeb1 = celeb1 if guess == 'a' else celeb2
                if input('would you like to continue : ').strip().lower()=='y':
                    continue
                else:
                    print(f'you quit with the score of {score}!')
                    break
            else:
                os.system('cls')
                print(f'Wrong! Final Score is {score}')
                print(f""" 
{celeb1[0]}: has {celeb1[1]} no of searches
{celeb2[0]}: has {celeb2[1]} no of searches""")
                go_again=input('\nwould you like to go again?Type (Y/N) : ').strip().lower()
                if go_again=='y':
                    continue
                else:
                    break
    compare()
highlow()   