from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(5)
        self.penup()