import os
import random
from art import logo, vs
from artist_data import artists_data
def highlow():
    def get_artist(exclude=None):
        celeb=random.choice(list(artists_data.items()))
        while exclude and celeb[0]==exclude[0]:
            celeb=random.choice(list(artists_data.items()))
        return celeb
    def format_printing(c1,c2):
        print(f""" 
Compare A : {c1[0]} with no of. searches: {c1[1]}
{vs}
Against B : {c2[0]} with no of. searches: ???
    """)
    def compare():
        score=0
        while True:
            celeb1=get_artist()
            print(logo)
            while True:
                celeb2=get_artist(exclude=celeb1)
                format_printing(celeb1,celeb2)
                guess=input('\nGuess which of the celeb has got more searches : ').strip().lower()
                if guess not in ['a','b']:
                    print('Enter a valid Character!')
                    continue
                if (guess=='a' and celeb1[1]>celeb2[1]) or (guess=='b'and celeb2[1]>celeb1[1]):
                    score+=1
                    os.system('cls') 
                    print(f'\nYou\'ve guess it right! your score is {score}')
                    celeb1=celeb1 if guess=='a' else celeb2
                    if input('\nwould you like to continue or leave here? (Y/N)').strip().lower()=='n':
                        print(f'\nYou quitted the final score is {score}!')
                        go_again=input('Would you like to go again? (Y/N)').strip().lower()
                    if go_again=='y':
                        break
                    else:
                        return
                else:
                    os.system('cls')
                    print(f'\nYou Lost with the final score of {score}')
                    print(f""" 
        {celeb1[0]}: has {celeb1[1]} no of searches
        {celeb2[0]}: has {celeb2[1]} no of searches""")
                    go_again=input('Would you like to go again? (Y/N)').strip().lower()
                    if go_again=='y':
                        break
                    else:
                        return
    compare()
highlow()
    