from turtle import Turtle
import math as mt
import turtle

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
        y=y-(mt.sqrt(3)*length)
        t.goto(-x_size,y)
        t.pd()


# Main Program

t=Turtle()

visited=[]

screen = turtle.Screen()
x=800
y=600
screen.setup(width=x, height=y)
# screen.setworldcoordinates(-400, -300, 400, 300)
t.pu()
t.goto(-x/2,y/2)
t.pd()
t.forward(x)
t.right(90)
t.forward(y)
t.right(90)
t.forward(x)
t.right(90)
t.forward(y)
t.right(90)

t.left(60)
t.speed(50)



t.pu()
t.goto(-(x/2),(y/2)-(mt.sqrt(3)*25))
t.pd()
honeycomb(x/2,y/2,50)

print(visited)
turtle.exitonclick()