from turtle import *

def draw_square(x_cordinate, y_cordinate):

    penup()
    goto(x_cordinate, y_cordinate)
    pendown()

    for i in range(4):
        forward(200)
        left(90)

draw_square(100, 100)
draw_square(-300,100)
draw_square(-300, -300)
draw_square(100, -300)














exitonclick()