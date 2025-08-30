""" Dictonary Comprehension Excercise """

string="what is the arispeed velocity of an uladen swallow"
# list=string.split()
result={word:len(word) for word in string.split()}
print(result)