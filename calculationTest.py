# Vital Nyabashi                    2/17/2023
# Lab Section 1
# In this file, we import the myTemps.py and myShape.py in one file (calculationTest.py. In that file we write programing to
# run myTemps and myShapes in one file location.



import myTemps
import myShapes

def main():
    while True:
        c = str(input("Pick functions: cubeVolumes,cubeSurface, sphereVolume, sphereSurface, kelvinToFahrenheit, fahrenheitToKelvin: "))
        if c == 'cubeVolumes':
            s = int(input("Pick number: "))
            x = myShapes.cubeVolume(s)
            print(x)
        elif c == 'cubeSurface':
            s = int(input("Pick number: "))
            x = myShapes.cubeSurface(s)
            print(x)
        elif c == 'sphereVolume':
            s = int(input("Pick number: "))
            x = myShapes.sphereVolume(s)
            print(x)
        elif c == 'sphereSurface':
            s = int(input("Pick number: "))
            x = myShapes.sphereSurface(s)
            print(x)
        elif c == 'kelvinToFahrenheit':
            s = int(input("Pick number: "))
            x = myTemps.kelvinToFahrenheit(s)
            print(x)
        elif c == 'fahrenheitToKelvin':
            s = int(input("Pick number: "))
            x = myTemps.fahrenheitToKelvin(s)
            print(x)
            return x
        else:
            print("ERROR")
main()

