# VITAL NAYABSHI             2/2/2023
# Lab Week 3/ SECTION A/ sphere surface: Ask the user for a single numerical number. Using the value, calculate the
# surface area using the sphere surface area formula (A= 4(pi)(r^2)

# Citation: https://www.cuemath.com/measurement/surface-area-of-sphere/
# Ask for the r value input



def sphereSurface():
    r = int(input("Enter single numerical value for radius: "))

    # Area= 4(pi)(r^2) pi= 3.14
    pi = 3.14
    Area = str(4 * pi * (r ** 2))

    # print the area of the sphere
    print(Area)

    return Area
