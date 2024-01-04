import random
import turtle

def tridecagonTurtle(t,s):
    for i in range(13):
        t.left(27+(9/13))
        t.forward(s)


def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'F':

        newstr = 'P-TFP+-F-F'   # Rule 1
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == 'T':
            # aTurtle.up()
            tridecagonTurtle(aTurtle,distance)

        elif cmd == 'P':
            aTurtle.up()
            ass = random.randint(1,360)
            butt = random.randint(1,100)
            aTurtle.goto(ass,butt)
            aTurtle.down()
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

def main():
    inst = createLSystem(4, "F")   # create the string
    print(inst)
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(1000)
    drawLsystem(t, inst, 80, 15)   # draw the picture
                                  # angle 60, segment length 5
    wn.exitonclick()

main()
