""" Ceasar's Cipher Day-08 """

def ceasar(start_text,shift_amount,cipher_direction):
    result_text=''
    if cipher_direction=='decode':
            shift_amount*=-1
    for letters in start_text:
        if letters in alphabets:
            position=alphabets.index(letters)
            new_position=position+shift_amount%26 
#%26 to keep the shift amount in bound of the total number of alphabets if thew user puts a number bigger than 26
            result_text+=alphabets[new_position]
        else:
            result_text+=letters
    print(f'The {cipher_direction}d text is: {result_text}')

end_program=False       
while not end_program:
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # The reason for repeating the elements in the list is if a word is starting from the letter "z" how can it be encoded if the list only got 26 indexes!
    direction=input('Type \"encode\" to encrypt your text and \"decode\" to decrypt\n')
    text=input('Enter the text:\n')
    shift=int(input('Enter the number you want to shift ahead your text to!\n'))
    ceasar(start_text=text,shift_amount=shift,cipher_direction=direction)
    go_again=input('Do you want to go again type \'yes\' to continue and \'no\' to exit:\n')
    if go_again=='no':
        end_program=True
        print('Goodbye')
         
""" A simpler but rather lenghty way of doing exact same thing """

# def encrypt(plain_text,shift_amount):
#     cipher_text=''
#     for letters in plain_text:
#         if letters in alphabets:
#             position=alphabets.index(letters)
#             new_position=position+shift_amount
#             new_letter=alphabets[new_position]
#             cipher_text+=new_letter
#         else:
#             cipher_text+=letters
#     print(cipher_text)
# def decrypt(plain_text,shift_amount):
#     deciphered_text=''
#     for letters in plain_text:
#         if letters in alphabets:
#             position=alphabets.index(letters)
#             new_position=position-shift_amount
#             new_letter=alphabets[new_position]
#             deciphered_text+=new_letter
#         else:
#             deciphered_text+=letters
#     print(deciphered_text)
# if direction=='encode':
#     encrypt(plain_text=text,shift_amount=shift)
# elif direction=='decode':   
#     decrypt(plain_text=text,shift_amount=shift)