from turtle import Turtle,Screen
import random
turtles={}
color=['yellow','green','red','black','purple','pink']
for i in range(1,6):
    turtles[i]=Turtle()
    turtles[i].shape('turtle')
    turtles[i].color(random.choice(color)) 

screen=Screen()
screen.listen()

screen.exitonclick()
