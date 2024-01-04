# VITAL NAYABSHI             2/2/2023
# Lab Week 3/ SECTION A/ cubeVolume: Ask the user for a single numerical number. Using the value, calculate the volume
# using the cubic formula (v= a^3)


#Citation: https://tutors.com/lesson/volume-of-a-cube
    # Python Dictionary
    # https://docs.python.org/3/library/math.html?highlight=cube



def cubeVolume():

    length = int(input("Enter single numerical value for length: "))

    volume = (length ** 3)

    print(volume)

    return volume
