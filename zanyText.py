# VITAL NAYABSHI             1/24/2023
# Lab Week 3/ SECTION A/ Zany Text!: Practice printing text strings, gathering input from the user with the input() function and concatending stings and input together

print("Zany Text!")
print()

print("By: VITAL NYABASHI")
print("COM S 127 section 1")

print()

#**********************************************************************************************************************************************************

# 'Zany Text' #1
print("Zany Text #1")

print()

noun1 = input("noun: ")
adjective1 = input("adjective: ")
adjective2 = input("adjective: ")
adjective3 = input("adjective: ")
verb1 = input("past tense verb: ")
noun2 = input("noun: ")
# Printing the final string
print("Once upon a time, there was a " +
        noun1 +
        ". It was a " +
        adjective1 + ", " +
        adjective2 + ", " +
        adjective3 + " " +
        noun1 +
        ". And, one day it " +
        verb1 + " " +
        "all over the " +
        noun2 + "!")
#**********************************************************************************************************************************************************
print()


# TODO: Make three additional 'Zany Texts' like the one above, and have all four

# 'Zany Text' #2 (2 pts.)
print("Zany Text #2")

print()

noun1 = input("What was your first pet's name or what would you name your  first pet?: ")
verb1 = input("What is your pet's favorite activity?: ")
verb2 = input("What another favorite activity?: ")
pronouns = input("What is your pet's pronouns? (ex. He or She): ")

print("My pet's name is " +noun1 + ". " +pronouns+ " loves to " + verb1 + " and " +verb2+ ".")
#**************************************************************************************************************
print()

print("Zany Text #3")
print()

order_roast= ''
order_size= ''
while order_size != 'small' and order_size != 'medium' and order_size != 'large':
    order_size = input('Pick the size you would like from the list (small/medium/large)?: ')

while order_roast != 'dark' and order_roast != 'medium' and order_roast != 'light':
    order_roast = input("Pick the roast you would like from the list(dark/medium/light)?: ")

costumer_name = input ('Enter your name: ')

print("You order of a " +order_size+ " , " +order_roast+ " roast coffee will be out to you soon. Please be pacient while we get it ready for you "
+costumer_name+ ".")

#**********************************************************************************************************************************************************
print()

print("Zany Text #4: Workout Plan")
print()
from datetime import date
today = date.today()

print(date.today())

workout_1 = input("What will be your 1st workout:")
workout_2 = input("What will be your 2nd workout :")
workout_3 = input("What will be your 3rd workout :")
workout_4 = input("What will be your 4th workout:")
run_distance= input("How many miles will you run?: ")

print("Today's date: ", today)
print("The 4 workouts on the workout program are " +workout_1+ ",then i will go and do " +workout_2+ ". After, I will do "
+workout_3+ ", and finally " +workout_4+". Then I will end it will a slow " +run_distance+ " mile run.")
#**********************************************************************************************************************************************************
