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
    snake.goto(position)
    snakes.append(snake)
game_is_on=True 
while game_is_on:
    screen.update()
    time.sleep(0.03)
    for snake in snakes:
        snake.forward(20)
screen.exitonclick()