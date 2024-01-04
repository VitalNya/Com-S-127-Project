

import turtle

def drawMultipleTridecagons(ben, s, x, y, nr, sr):
    ben.goto(x,y)
    ben.down()
    for i in range (nr):
        for i in range(13):
            ben.left(27 + (9 / 13))
            ben.forward(s)
        ben.up()
        ben.forward(sr)
        ben.down()

size = int(input("Enter a number"))  # lenght of one sides of the regular tridecagon
x_cor = int(input("Enter a number")) # (x, ) coordinate
y_cor = int(input("Enter a number")) # ( ,y) coordinate
number_tri = int(input("Enter a number for number of tridecagon repetitions: "))
space = int(input("Enter a number for amount of space between tridecagon repetitions on the 'x' axis: "))
sr = x_cor + space

wn = turtle.Screen()
ben= turtle.Turtle()
ben.up()
drawMultipleTridecagons(ben,size,x_cor,y_cor,number_tri,sr)

wn.exitonclick()
