""" OOP Class() breakdown """
# class User:
#     pass

# user_1=User()   
# user_1.id=1
# user_1.username='Usman Junaidy'
# print(f"{user_1.username}, {user_1.id:03d}")
# user_2=User()   
# user_2.id=4
# user_2.username='Ali'

""" __innit__(self) constructor (initializer) """

# class User:
#     def __init__(self, user_id, username):
#         self.id=user_id
#         self.username=username
#         self.followers=0 #Passing a attribute that might contain a default value!

# user_1=User('003','Usman Junaidy')   
# user_2=User('500','Tony Stark')
# print(user_1.username, user_1.id, user_1.followers)
# print(user_2.username, user_2.id)

""" Methods """
class User:
    def __init__(self, user_id, username):
        self.id=user_id
        self.username=username
        self.followers=0 #Passing a attribute that might contain a default value!
        self.following=0 #Passing a attribute that might contain a default value!
    def follow(self, user):
        user.followers+=1
        self.following+=1
 
 
user_1=User('003','Usman Junaidy')   
user_2=User('004','Ali Junaidy')   
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
