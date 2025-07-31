from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score=0
        self.write(f'Scoreboard{self.score}',False,'center',('Arial',8,'normal'))
