import random
listofwords=["bulldog",'germanshepard','husky']
chosenword=random.choice(listofwords)
print(chosenword)
display=['_' for dog in chosenword]
print(','.join(display))
while '_' in display:
    guess=input("Guess a letter!\t").lower()
    for position in range(len(chosenword)):
        letter=chosenword[position]
        if letter==guess:
            display[position]=letter
    print(','.join(display))
