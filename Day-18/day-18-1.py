from turtle import *
jd=Turtle()
for i in range(4):
    jd.forward(100)
    jd.right(90)

screen=Screen()
screen.exitonclick()

""" Implemented the use of * while importing modules """
from random import *
list=[1,2,3,4,5,6]
computerchoice=choice(list)
print(computerchoice)

""" Giving Modules an Alias name """
import turtle as t
tim=t.Turtle()

""" Drawing a Dashed line in turtle """
from turtle import *
jd=Turtle()
for i in range(4):
    jd.forward(100)
    jd.right(90)

screen=Screen()
screen.exitonclick()

""" Making a square using dashed lines """
from turtle import Turtle, Screen
tt= Turtle()
for j in range(4):
    for _ in range(10):
        tt.forward(10)
        tt.penup()
        tt.forward(10)
        tt.pendown()
    tt.right(90)
screen = Screen()
screen.exitonclick()

""" Drawing 8 basic shapes using turtle graphics """
from turtle import Turtle, Screen
import random
colors = [
    "red", "blue", "green", "yellow", "purple",
    "orange", "pink", "black", "gray", "brown",
    "cyan", "magenta", "gold", "silver", "navy",
    "lime", "maroon", "turquoise", "violet", "indigo"
]
jdy=Turtle()
def draw_shape(sides):
    angle=360/sides
    for i in range(sides):
        jdy.forward(100)
        jdy.right(angle)
for shapes_side in range(3,11):
    jdy.color(random.choice(colors))
    draw_shape(shapes_side)
screen=Screen()
screen.exitonclick()