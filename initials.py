# VITAL NAYABSHI             2/2/2023
# Lab Week 3/ SECTION A/ initials: Using the turtle command, draw a picture of VN (initials : first and last) then
# coloring in the initials so the initials is a different color for your background


import turtle
wn = turtle.Screen()
x = turtle.Turtle()


x.color('red', 'blue')
x.begin_fill()
x.right(180) #THE LETTER V
x.forward(30)
x.right(60)
x.forward(100)
x.right(120)
x.forward(30)
x.right(60)
x.forward(70)
x.left(120)
x.forward(70)
x.right(60)
x.forward(30)
x.right(120)
x.forward(100)
x.up()
x.left(120)
x.forward(60)

x.down()


x.left(90) # THE LETTER N
x.forward(87)
x.right(90)
x.forward(30)
x.right(60)
x.forward(70)
x.left(150)
x.forward(64)
x.right(90)
x.forward(20)
x.right(90)
x.forward(87)
x.right(90)
x.forward(30)
x.right(60)
x.forward(67)
x.left(60)
x.left(90)
x.forward(60)
x.right(90)
x.forward(22)
x.end_fill()


turtle.done()
