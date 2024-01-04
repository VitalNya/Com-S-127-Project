# VITAL NAYABSHI             2/2/2023
# Lab Week 4/ SECTION A/
import random
def randomSum(a,b,c):
    b = b + 1
    sum = 0

    for x in range(c):
        vital =  random.randrange(a,b)
        sum = sum + vital
    return sum



a = int(input("Pick a number: "))
b = int(input("Pick a number: "))
c = int(input("Pick a number: "))

d = randomSum(a,b,c)
print("The result of randomSum({0},{1},{2}) = {3}".format(a, b, c, d))






