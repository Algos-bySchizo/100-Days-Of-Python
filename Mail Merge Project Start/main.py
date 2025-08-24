with open("Input/Names/invited_names.txt") as file:
    names=[name.strip() for name in file.readlines()]
    print(names)
with open('Input/Letters/starting_letter.txt') as file:
    letter=file.read()
    letter.strip()
    for name in names: 
        with open(f'Output/ReadyToSend/{name}_invitation.txt','w') as file :
            file.write(letter.replace('[name]',name))
 