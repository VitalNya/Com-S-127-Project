# VITAL NAYABSHI             2/2/2023
# Lab Week 3/ SECTION A/ Sphere volume: Ask the user for a single numerical number. Using the value, calculate the
# volume using the sphere volume equation (V=(4/3)(pi)(r^3)

# citation: https://byjus.com/maths/volume-of-sphere/
# Ask for the r value input


def sphereVolume():
    r = int(input("Enter single numerical value for radius: "))

    # volume = 4/3(pi)(r^3) pi= 3.14
    pi = 3.14
    volume = (4 / 3) * (pi) * (r ** 3)

    # print the area of the sphere
    print(volume)

    return volume
