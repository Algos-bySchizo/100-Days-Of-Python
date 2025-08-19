from turtle import Turtle
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.goto(-290,260)
        self.write(f'Score:{self.score}',False,'left',FONT)
    
    def increase_score(self):
        self.clear()
        self.score+=1
        self.write(f'Score:{self.score}',False,'left',FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write('Game Over 😝',False,'center',FONT)