from turtle import Turtle
FONT = ("Courier", 18, "normal")
SCORE=0

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-290,260)
        self.write(f'Score:{SCORE}',False,'left',FONT)
    
    def increase_score(self):
        SCORE+1
        self.write(f'Score:{SCORE}',False,'left',FONT)