# <Vital Nyabashi> <2/10/223>
# <Assignment #2 / Lab 1/ etc.>
# User is given 3 options 'c','l','q' and 'q'. Each of those options will result in a different outcome.
# One option (c) will ask the use for two numbers then another for a mathematical symbol used for the two numbers.
# Another option (l) will take the two integers the user inputted from part 'c' and compare the numbers with a random number
# the computer generates for us. Whether the random number is bigger or small than the inputted number will determine what we do next.


import random

def Calculator(c, x_1, x_2):
    if c == '+':
        answer = x_1 + x_2
        return answer

    elif c == '*':
        answer = x_1 * x_2
        return answer

    elif c == '-':
        answer = ((x_1) - (x_2))
        return answer

    elif c == '/':
        if x_2 == 0:
            print("error")
            x_2 = 1
        answer = x_1 / x_2
        return answer

    elif c == '//':
        if x_2 == 0:
            print("error")
            x_2 = 1
        answer = x_1 // x_2
        return answer

    elif c == '%':
        if x_2 == 0:
            print("error")
            x_2 = 1
        answer = x_1 % x_2
        return answer
    elif c == '**':
        answer = x_1 ** x_2
        return answer


def luckNumber(num1,num2):
    ops = ['+', '-', '*', '/']
    operation = random.choice(ops)
    returned = Calculator(operation, num1, num2)
    python()
    x = ("The result of your calculation was: {0}, {1}, {2} = {3}". format( num1 , operation, num2, returned))
    return x


print("Lucky Calculator")
print()
print("By: <Vital Nyabashi>")
print("[COM S 127 <A>]")
print()
print("What would you like to do?")
print()
choice = input("[c]alculator, [l]ucky number, [q]uit: ")
print()
if choice == 'c':
    number1 = int(input("Choose first integer"))
    number2 = int(input("Choose second integer"))
    option = input("Choose calculations: [+], [-], [*], [/], [//], [%], [**]: ")
    returned = Calculator(option, number1, number2)
    print("The result of your calculation was: {0}, {1}, {2} = {3}". format( number1 , option, number2, returned))
    result = number1


if choice == 'l':
    number1= int(input("Enter an integer: "))
    number2= int(input("Enter an integer: "))
    x = luckNumber(number1,number2)
    print(x)


elif choice == "q":
    print("Goodbye!")

else:
    print("ERROR: ANSWER NOT APPROPRIATE. TRY AGAIN!")