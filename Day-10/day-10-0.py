""" Functions With Outputs """
def format_name(fname, lname):
     result=fname.title()+' '+lname.title()
     return f"{result}"
formatted_string=format_name(input('what is your first name? '),input('what is your last name?'))
print(formatted_string)
