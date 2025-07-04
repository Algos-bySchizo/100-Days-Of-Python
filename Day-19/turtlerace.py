from turtle import Turtle,Screen
import random
colors_list= ['red', 'blue', 'green', 'orange', 'purple', 'pink']
screen=Screen()
screen.colormode(255)
screen.setup(width=500,height=400)
start_y= -100
users_bet=screen.textinput('Place a bet','Enter the turtle you think will win!') 
screen.listen()
turtle_list=[]
for i in range(6):
    t=Turtle(shape='turtle')
    t.color(colors_list[i])
    t.penup()
    t.goto(x=-230, y=start_y + i * 40)
    turtle_list.append(t)
screen.exitonclick()