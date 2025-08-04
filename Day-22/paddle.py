from turtle import Turtle
STARTING_POS=[(350,0),(-350,0)]

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddles=[]

    def create_paddle(self):
        for position in STARTING_POS:
         self.append_pad(position)
    
    def append_pad(self, position):
        paddle=Turtle('square')
        paddle.shapesize(5,1)
        paddle.color('white')
        paddle.penup()
        paddle.goto(position)
        self.paddles.append(paddle)