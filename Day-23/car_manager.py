from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.allcars=[]
    
    def create_car(self):
        new_car=Turtle('square')
        new_car.shapesize(1,2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.setheading(180)
        new_car.goto(300-STARTING_MOVE_DISTANCE,random.randint(-250,250))
        self.allcars.append(new_car)
    
    def move_cars(self):
        for car in self.allcars:
            car.forward(STARTING_MOVE_DISTANCE)