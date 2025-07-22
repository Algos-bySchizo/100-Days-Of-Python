from turtle import Turtle
STARTING_COORDINATES=[(0,0),(-20,0),(-40,0)]
PACE=20
class Snake:
    def __init__(self):
        self.snakes=[]
        self.create_snake()
    def create_snake(self):
        for position in STARTING_COORDINATES:
            snake=Turtle('square')
            snake.color('white')
            snake.penup()
            snake.goto(position)
            self.snakes.append(snake)
    def move(self):
        for snake in range(len(self.snakes)-1,0,-1):
                last_snake_x=self.snakes[snake-1].xcor()
                last_snake_y=self.snakes[snake-1].ycor()
                self.snakes[snake].goto(last_snake_x,last_snake_y)
        self.snakes[0].forward(PACE)