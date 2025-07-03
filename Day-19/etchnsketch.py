from turtle import Turtle,Screen
tit=Turtle()
screen=Screen()
def move_forwards():
    tit.forward(20)
def move_backwards():
    tit.backward(20)
def move_right():
    tit.right(20)    
def move_left():
    tit.left(20)
screen.listen()
screen.onkey(move_forwards,'w')
screen.onkey(move_backwards,'s')
screen.onkey(move_right,'d')
screen.onkey(move_left,'a')
screen.onkey(tit.reset,'c')
screen.listen()
screen.exitonclick()