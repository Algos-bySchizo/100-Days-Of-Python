""" How to open and read a text file's content and print it """

file = open('record_file.txt')
content=file.read()
print(content)
file.close()

""" Opening a file using "with" args "as" args """
with open('record_file.txt') as file:
    content=file.read()
    print(content)

""" Opening an editable file using "with" args "as" args """
with open('record_file.txt','w') as file:
    file.write('add thisnew text to file!')
    
