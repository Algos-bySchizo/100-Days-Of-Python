from turtle import Turtle,Screen
import random
tit=Turtle()
screen=Screen()
colors = [
    "red", "blue", "green", "yellow", "purple",
    "orange", "pink", "black", "gray", "brown",
    "cyan", "magenta", "gold", "silver", "navy",
    "lime", "maroon", "turquoise", "violet", "indigo"
]
directions=[0,90,180,270]
walk_not=True
for i in range(500):
    tit.speed('fastest')
    tit.width(10)
    tit.color(random.choice(colors))
    tit.forward(30)
    tit.setheading(random.choice(directions))
screen.exitonclick()