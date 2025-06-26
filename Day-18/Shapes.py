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