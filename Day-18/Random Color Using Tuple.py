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

directions=[0,90,180,270]
walk_not=True
for i in range(500):
    tit.speed('fastest')
    tit.width(10)
    tit.color(random_color())
    tit.forward(30)
    tit.setheading(random.choice(directions))
screen.exitonclick()