from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore=0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.write(f'Score: {self.score} HighScore: {self.highscore}',False,'center',('Arial',12,'normal'))
    
    def update_scoreboard(self):
        self.clear()
        self.goto(0,280)
        self.write(f'Score: {self.score} HighScore: {self.highscore}',False,'center',('Arial',12,'normal'))
    
    def increase_score(self):
        self.score+=1
        self.update_scoreboard()
    
    # def game_over(self):
    #     self.goto(0,280)
    #     self.update_scoreboard()
    
    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
        self.score=0
        self.update_scoreboard()