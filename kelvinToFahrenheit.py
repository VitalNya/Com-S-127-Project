# VITAL NAYABSHI             2/2/2023
# Lab Week 3/ SECTION A/ kelvins to Fahrenheit: Ask the user for a single numerical number. Using the value, calculate
# the temperature using the equation F = 9/5(K - 273) + 32

# citation:https://www.thoughtco.com/convert-kelvin-to-fahrenheit-609234#:~:text=The%20easiest%20formula%20for%20converting,It%20does%20not%20have%20degrees.
# kelvin to Fahrenheit conversion formula: K= (F-32)*(5/9)+273.15
# K = kelvin
# F = Fahrenheit




def kelvinToFahrenheit():
    K = int(input("Enter single numerical value for Kelvin: "))

    F = (9 / 5 * (K - 273) + 32)

    print(F)

    return F
