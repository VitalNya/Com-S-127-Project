# Vital Nyabashi                    2/17/2023
# Lab Section 1
# In this file, we make functions to calc. a sphere's volume, sphere's surface area, cube surface area, and cube volume.

def sphereVolume(r):

    # volume = 4/3(pi)(r^3) pi= 3.14
    pi = 3.14
    volume = (4 / 3) * int(pi) * (r ** 3)
    return volume

def sphereSurface(r):

    # Area= 4(pi)(r^2) pi= 3.14
    pi = 3.14
    area = str(4 * pi * (r ** 2))
    # area1 = ("Your sphere surface is " + area)

    return area

def cubeSurface(edge):
    # Area= 6(edge^2)
    area = 6 * (edge ** 2)
    # area1= ("Your cube surface is " + area)
    return area

def cubeVolume(length):
    volume = (length ** 3)
    # volume1= ("Your cube volume is " + volume)
    return volume




