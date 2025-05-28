import os
bids={}
bidding_finish=False
bidding_record={}
def find_highest_bidder(bidding_record):
    winner=''
    highest_bid=0
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f'The winner is {winner} with the highest bid of ${highest_bid}')

while not bidding_finish:
    name=input('what\'s your name?\n')
    bid=int(input('what\'s your bid price?\n'))
    bids[name]= bid
    add_other_bidder=input('is there anyone else that would like to bid?\n').lower()
    if add_other_bidder=='yes':
        os.system('cls')
        continue
    else:
        bidding_finish=True
        find_highest_bidder(bids)



















# import os
# bidders_name=input("what's your name?")
# biddes_bid=input('what\'s your bid price?')
# bidders_list=[{}]
# def add_new_bidders(bidders_name,bidders_bid):
#     another_bidder=True
#     while not another_bidder:      
#         bidders={}
#         bidders["bidder's name"]=bidders_name
#         bidders["bidder's bid"]=bidders_bid
#         bidders_list.append(bidders)
#         print(bidders)
#         add_bidder=input('is there anyone else who wants to bid?').lower()
#         if add_bidder=='yes':
#             os.system('cls')
#             bidders_name=input("what's your name?")
#             bidders_bid=input('what\'s your bid price?')
#         else:
#             another_bidder=False
