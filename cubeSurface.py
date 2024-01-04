# VITAL NAYABSHI             2/2/2023
# Lab Week 3/ SECTION A/ cube surface area: Ask the user for a single numerical number. Using the value, calculate the
# surface area using the cube surface area equation a=6(edge^2)

# Citation: https://www.cuemath.com/measurement/surface-area-of-cube/
# Ask for the r value input



def cubeSurface():
    edge = int(input("Enter single numerical value for edge lenghth: "))

    # Area= 6(edge^2)
    Area = 6 * (edge ** 2)
    # print the area of the sphere
    print(Area)

    return Area
