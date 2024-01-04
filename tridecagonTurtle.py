

import turtle


def tridecagonTurtle(t,s,x,y):
    t.goto(x,y)
    t.down()
    for i in range(13):
        t.left(27+(9/13))
        t.forward(s)

size = int(input("Enter a number"))  # lenght of one sides of the regular tridecagon
x_cor = int(input("Enter a number")) # (x, ) coordinate
y_cor = int(input("Enter a number")) # ( ,y) coordinate

wn = turtle.Screen()
ben= turtle.Turtle()
ben.up()
tridecagonTurtle(ben, size,x_cor,y_cor)

wn.exitonclick()