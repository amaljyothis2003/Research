from turtle import Turtle
import math as mt
import turtle

full_hexa=0

def draw_hexagon(size):
    for i in range(0,9):
        t.forward(size)
        t.right(60)
    # full_hexa+=1
        

def honeycomb(x_size,y_size, length):
    for i in range(0,(int)(y/(mt.sqrt(3)*length))):
        for j in range(1,(int)(x/((5/2)*length))):
            draw_hexagon(length)
            x1,y1=t.pos()
            visited.append(t.pos())
            t.goto(x1+length,y1)
            t.left(180)
        t.pu()
        y1=y1-(mt.sqrt(3)*length)
        t.goto(-x_size,y1)
        t.pd()


# Main Program

t=Turtle()

visited=[]

screen = turtle.Screen()
x=int(input("Enter the x value: "))
y=int(input("Enter the y value: "))
length=int(input("Enter the lenght of the regular hexagon:"))
screen.setup(width=x, height=y)
# screen.setworldcoordinates(-x, -y, x, y)
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
t.goto(-(x/2),(y/2)-(mt.sqrt(3)*length/2))
t.pd()
honeycomb(x/2,y/2,length)

# print("Area of Full Hexagon: ",)

print(visited)
turtle.exitonclick()