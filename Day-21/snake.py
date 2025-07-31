from turtle import Turtle
STARTING_COORDINATES=[(0,0),(-20,0),(-40,0)]
PACE=20
class Snake:
    def __init__(self):
        self.snakes=[]
        self.create_snake()
        self.head=self.snakes[0]
    def create_snake(self):
        for position in STARTING_COORDINATES:
            snake=Turtle('square')
            snake.color('black')
            snake.penup()
            snake.goto(position)
            self.snakes.append(snake)
    def move(self):
        for snake in range(len(self.snakes)-1,0,-1):
                last_snake_x=self.snakes[snake-1].xcor()
                last_snake_y=self.snakes[snake-1].ycor()
                self.snakes[snake].goto(last_snake_x,last_snake_y)
        self.snakes[0].forward(PACE)
    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)
    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)