""" Black Jack Game """
import random
import os
def blackjack():
    while True:
        def compare(user_score,dealers_score):
            """ This compares the score of dealer and user """
            if user_score== dealers_score:
                return 'draw 😕'
            elif dealers_score==0:
                return "you lost the game dealer\'s got a blackjack"
            elif user_score==0:
                return "you won the game you got a blackjack"
            elif user_score>21:
                return "you lost the game you went over 21 pts"
            elif dealers_score>21:
                return "you won the game dealer went over 21 pts"
            elif user_score>dealers_score:
                return "You won!"
            else:
                return "You lost!"
        def calculate_score(cards):
            """ It takes list of cards and calculates the score of the cards! """
            if sum(cards)==21 and len(cards)==2:
                return 0
            if 11 in cards and sum(cards)>21:
                cards.remove(11)
                cards.append(1)
            return sum(cards)
        def hand_card():
            """ It took a random card from the deck and returns it a card to the hand!"""
            cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
            card=random.choice(cards)
            return card
        users_hand=[]
        dealers_hand=[]
        game_over=False
        for _ in range(2):
            users_hand.append(hand_card())
            dealers_hand.append(hand_card())
        while not game_over:
            user_score=calculate_score(users_hand)
            dealers_score=calculate_score(dealers_hand)
            display=["_" if i==0 else dealers_hand[i] for i in range(len(dealers_hand))]
            print(f"your cards are {users_hand} and current score is: {user_score}\n")
            print(f"Dealer\'s hand are {display}\n")
            if user_score==0 or dealers_score==0 or user_score>21:
                game_over=True
            else:
                add_card=input('\ndo you want to add another card or pass? (Y/N): ').lower()
                if add_card=='y':
                    users_hand.append(hand_card())
                else:
                    game_over=True
        while dealers_score!=0 and dealers_score<17:
            dealers_hand.append(hand_card())
            dealers_score=calculate_score(dealers_hand)
        print(f"User's final hand is {users_hand} and total score is {user_score}\n")
        print(f"Dealer's final hand is {dealers_hand} and total score is {dealers_score}\n")
        print(compare(user_score,dealers_score))
        go_again=input("would you like to play again? (Y/N) :").lower()
        if go_again!='y':
            os.system('cls')
            print('Exited!')
            return False
blackjack()
