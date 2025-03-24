""" Ceasar's Cipher Day-08 """
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction=input('Welcome to Ceasar\'s Cipher type \"encode\" to encrypt your text and \"decode\" to decrypt')
text=input('Enter the text you want to encrypt')
shift=int(input('Enter the number you want to shift ahead your text to!'))
def encrypt(plain_text,shift_amount):
    cipher_text=''
    for letters in plain_text:
        position=alphabets.index(letters)
        new_position=position+shift_amount
        new_letter=alphabets[new_position]
        cipher_text+=new_letter
    print(cipher_text)
def decrypt(plain_text,shift_amount):
    deciphered_text=''
    for letters in plain_text:
        position=alphabets.index(letters)
        new_position=position-shift_amount
        new_letter=alphabets[new_position]
        deciphered_text+=new_letter
    print(deciphered_text)

if direction=='encode':
    encrypt(text,shift)
    
    for 
elif direction=='decode':   
    text=input('Enter the text you want to decrypt')
    shift=int(input('Enter the number you want to shift ahead your text to!'))
