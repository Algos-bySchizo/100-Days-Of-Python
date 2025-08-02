from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('white')
screen.title('Snake Xenxia')
screen.tracer(0)
snake=Snake()
score=Scoreboard()
food = Food()
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')
game_is_on=True 
while game_is_on:
    screen.update()
    time.sleep(0.06)
    snake.move()
    if snake.head.distance(food)<18:
        food.refresh()
        score.increase_score()
    if snake.head.xcor()>300 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-300:
        score.game_over()
        game_is_on=False
screen.exitonclick()