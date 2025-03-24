import random
word_list=['python','java','c language']
chosen_word=random.choice(word_list)
print(chosen_word)
""" One way of writing _ instead of lettters """
display=[]
for evrylttr in chosen_word:
    evrylttr="_"
    display+=evrylttr
print(display)

"""  two way of writing _ instead of lettters """
display2=[]
for _ in range(len(chosen_word)):
    display2+="*"
print(display2)

""" way three of writing _ instead of lettters """
display3=["___" for n in chosen_word]
print(",".join(display3))

""" way four of writing _ instead of lettters """
display4=['_']*len(chosen_word)
print(''.join(display4))