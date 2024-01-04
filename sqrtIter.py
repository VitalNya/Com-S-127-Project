# VITAL NAYABSHI             2/2/2023
# Lab Week 4/ SECTION A/


# Citation: https://www.cuemath.com/algebra/square-root-of-2/
# Formula: ((x/y)+y)/2



def sqtIter(x,iterations):
    y = (x + 1) / 2.
    initial_guess = ((int(x) / int(y)) + y) / 2

    for i in range(iterations):
        y = ((x / y) + y) / 2

    return (y)



x = int(input("pick a number: "))
iterations = int(input("pick a number: "))
d = sqtIter(x,iterations)
print("The result of sqtIter({0},{1}) = {2}".format(x, iterations, d))