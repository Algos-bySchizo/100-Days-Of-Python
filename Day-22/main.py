from turtle import Screen
from paddle import Paddle
screen=Screen()
screen.title('Ping Pong')
screen.bgcolor('black')
screen.setup(800,600)
screen.tracer(0)

paddles=Paddle()
paddles.create_paddle()

def go_up():
    new_y=paddles.paddles[0].ycor()+20
    paddles.paddles[0].goto(350,new_y)

def go_down():
    new_y=paddles.paddles[0].ycor()-20
    paddles.paddles[0].goto(350,new_y)

screen.listen()
screen.onkey(go_up,'Up')
screen.onkey(go_down,'Down')

game_is_on=True
while game_is_on:
    screen.update()

screen.exitonclick()
