from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=500,height=400)
start_y= -100
colors_list= ['red', 'blue', 'green', 'orange', 'purple', 'pink']
users_bet=screen.textinput('Place a bet','Enter the turtle you think will win!') 
turtle_list=[]
for i in range(6):
    t=Turtle(shape='turtle')
    t.color(colors_list[i])
    t.penup()
    t.goto(x=-230, y=start_y + i * 40)
    turtle_list.append(t)
if users_bet:
    is_race_on=True
    while is_race_on:
        for turtle in turtle_list:
            if turtle.xcor()>230:
                is_race_on=False
                winning_color=turtle.pencolor()
                if winning_color==users_bet:
                    print(f'You\'ve won the bet, The {winning_color} Turtle is the winner!')
                else:
                    print(f"you've lost the bet,  The {winning_color} Turtle is the winner!")
            pace=random.randint(0,10)
            turtle.forward(pace)
screen.exitonclick()