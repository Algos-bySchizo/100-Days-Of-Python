from turtle import Screen, Turtle
# from paddle import Paddle
screen=Screen()
screen.title('Ping Pong')
screen.bgcolor('black')
screen.setup(800,600)
pad1=Turtle()
pad1.shape('square')
pad1.color('white')
pad1.shapesize(5,1)
pad1.penup()
pad1.goto(350,0)
def go_up():
    new_y=pad1.ycor()+20
    pad1.goto(350,new_y)
def go_down():
    new_y=pad1.ycor()-20
    pad1.goto(350,new_y)

screen.listen()
screen.onkey(go_up,'Up')
screen.onkey(go_down,'Down')
screen.exitonclick()
