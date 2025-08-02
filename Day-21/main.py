from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
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
    time.sleep(0.05)
    snake.move()
    if snake.head.distance(food)<18:
        food.refresh()
        snake.new_seg()
        score.increase_score()
    if snake.head.xcor()>300 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-300:
        score.game_over()
        game_is_on=False
    for segs in snake.snakes[1:]:
        if snake.head.distance(segs)<10:
            score.game_over()
            game_is_on=False
screen.exitonclick()