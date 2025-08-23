# """ How to open and read a text file's content and print it """

# file = open('record_file.txt')
# content=file.read()
# print(content)
# file.close()

# """ Opening a file using "with" args "as" args """
# with open('record_file.txt') as file:
#     content=file.read()
#     print(content)

# """ Opening and writing in a file using "with" args "as" args """
# with open('record_file.txt','w') as file:
#     file.write('add thisnew text to file!')
    
# """ Opening and editing/adding contect in a file using "with" args "as" args """
# with open('record_file.txt','a') as file:
#     file.write('add thisnew text to file!')

# # Important thing is if you don't have a file made on the folder and you run this ⬇️
# #  with open('record_file.txt','a') as file: it will create a new file with that name

""" Opening a file which is out of the current directory """

with open("/Users/JUNAIDY'S/OneDrive/Desktop/new_txt_file.txt") as file:
    content=file.read()
    print(content)