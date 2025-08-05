from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()
screen.title('Ping Pong')
screen.bgcolor('black')
screen.setup(800,600)
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,'Up')
screen.onkey(r_paddle.go_down,'Down')
screen.onkey(l_paddle.go_up,'w')
screen.onkey(l_paddle.go_down,'s')

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()==300 or ball.ycor()==-300:
        ball.bounce()
    if ball.distance(r_paddle)<55 and ball.xcor()>320 or ball.distance(l_paddle)<55 and ball.xcor()<-320:
        ball.deflect()
    if ball.xcor()>380:
        ball.restartpos()
        scoreboard.l_point()
    if ball.xcor()<-380:
        ball.restartpos()
        scoreboard.r_point()
    
screen.exitonclick()
