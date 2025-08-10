from turtle import Turtle
import math as mt
import turtle

t=Turtle()

visited=[]

screen = turtle.Screen()
screen.setup(width=800, height=600)
# screen.setworldcoordinates(-400, -300, 400, 300)
t.pu()
t.goto(-400,300)
t.pd()
t.forward(800)
t.right(90)
t.forward(600)
t.right(90)
t.forward(800)
t.right(90)
t.forward(600)
t.right(90)

t.left(60)
t.speed(50)


def draw_hexagon(size):
    for i in range(0,9):
        t.forward(size)
        t.right(60)
        

def honeycomb(x_size,y_size, length):
    for i in range(0,5):
        for j in range(0,5):
            draw_hexagon(length)
            x,y=t.pos()
            visited.append(t.pos())
            t.goto(x+length,y)
            t.left(180)
        t.pu()
        t.goto(-x_size,y_size-(mt.sqrt(3)*length))
        y_size=y_size-(mt.sqrt(3)*length)
        t.pd()

t.pu()
t.goto(-400+50,300+50)
t.pd()
honeycomb(400,300,50)

print(visited)
turtle.exitonclick()