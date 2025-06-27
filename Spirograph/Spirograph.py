from turtle import Turtle,Screen
import random
tit=Turtle()
screen=Screen()
screen.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color_tuple=(r,g,b)
    return color_tuple
tit.speed('fastest')
def draw_spirograph(gap):
    for i in range (int(360/gap)):
        tit.color(random_color())
        tit.circle(100)
        tit.right(gap)
draw_spirograph(5)
screen.exitonclick()