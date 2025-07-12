from turtle import Turtle,Screen
tit=Turtle()
screen=Screen()
def move_forward():
    tit.forward(10)
screen.onkey(key='space', fun=move_forward)
screen.listen()
screen.exitonclick()    