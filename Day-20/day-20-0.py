from turtle import Turtle,Screen,Shape
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Xenxia')
screen.tracer(0)
starting_positions=[(0,0),(-20,0),(-40,0)]
snakes=[]
for position in starting_positions:
    snake=Turtle('square')
    snake.color('white')
    snake.penup()
    snakes.append(snake)
    snake.goto(position)
game_is_on=True 
while game_is_on:
    screen.update()
    time.sleep(0.03)
    for snake in range(len(snakes)-1,0,-1):
        last_snake_x=snakes[snake-1].xcor()
        last_snake_y=snakes[snake-1].ycor()
        snakes[snake].goto(last_snake_x,last_snake_y)
    snakes[0].forward(20)
screen.exitonclick()