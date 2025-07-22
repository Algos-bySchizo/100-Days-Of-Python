from turtle import Turtle,Screen,Shape
screen=Screen()
poly=((0,0),(10,-5),(0,10),(-10,-5))
s=Shape('compound')
s.addcomponent(poly,'red',"blue")
screen.register_shape("custom",s)

t=Turtle()
t.shape('custom')


# snake=Turtle(shape='square')

screen.exitonclick()