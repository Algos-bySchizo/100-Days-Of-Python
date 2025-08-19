import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player=Player()
obs=CarManager()
score=Scoreboard()
screen.onkey(player.move,'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    obs.create_car()
    obs.move_cars()
    for car in obs.allcars:
        if car.distance(player)<20:
            game_is_on=False 
            score.game_over()
    if player.is_at_finish_line():
        player.go_to_start()
        obs.level_up()
        score.increase_score()
screen.exitonclick()