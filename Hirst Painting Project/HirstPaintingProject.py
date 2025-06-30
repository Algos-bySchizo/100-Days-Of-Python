# import colorgram
# colors=colorgram.extract('download.jpg',30)
# color=[]
# for i in range(len(colors)):
#     clr=colors[i].rgb
#     color.append((clr.r,clr.g,clr.b))
# print(color)
from turtle import Turtle,Screen
import random
tit=Turtle()
screen=Screen()
screen.colormode(255)
color_list=[(198, 165, 116), (144, 79, 55),
             (221, 201, 138), (58, 93, 121), (167, 153, 48), (132, 34, 23), (137, 162, 181), (69, 40, 34),
               (51, 117, 87), (195, 93, 75), (146, 178, 150), (18, 93, 72), (231, 176, 165), (162, 143, 158)
               , (35, 60, 75), (105, 73, 77), (180, 204, 177), (148, 19, 23), (83, 147, 127), (70, 37, 40),
                 (18, 70, 60), (27, 82, 88), (40, 66, 89), (190, 86, 89), (68, 64, 58), (223, 176, 180)]
tit.hideturtle()
tit.setheading(225)
tit.penup()
tit.forward(400)
tit.setheading(0)
tit.showturtle()
tit.speed('fastest')
number_of_dot=100
for dot_count in range(1,number_of_dot+1):
    tit.dot(20,random.choice(color_list))
    tit.forward(50)
    if dot_count%10==0:
        tit.setheading(90)
        tit.penup()
        tit.forward(50)
        tit.left(90)
        tit.forward(500)
        tit.setheading(0)
screen.exitonclick()
