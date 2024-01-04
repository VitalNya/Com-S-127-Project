
# VITAL NAYABSHI             2/2/2023
# Lab Week 3/ SECTION A/ Fahrenheit to kelvins : Ask the user for a single numerical number. Using the value, calculate
# the surface area using the equation K= (F-32)*(5/9)+273.15


# citation: https://www.cuemath.com/fahrenheit-to-kelvin-formula/
# Fahrenheit to kelvin conversion formula: K= (F-32)*(5/9)+273.15
# K = kelvin
# F = Fahrenheit



def fahrenheitToKelvin():
    F = int(input("Enter single numerical value for Degree Fahrenheit: "))

    K = (F - 32) * (5 / 9) + (273.15)

    print(K)

    return K

