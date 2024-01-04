# Vital Nyabashi                    2/17/2023
# Lab Section 1
# In this file, we make functions for fahrenheit to kelvin and kelvin to fahrenheit.


def fahrenheitToKelvin(F):

    K = int(F - 32) * (5 / 9) + 273.15

    return K

def kelvinToFahrenheit(K):

    F = (9 / 5 * int(K - 273) + 32)

    return F
