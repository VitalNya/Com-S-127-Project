# # <Vital Nyabashi>             <2/21/2023>
# # <Assignment 3/ Lab A/ etc.>
# # <This is a multiplayer game. The user has the option to play 2 player game or just one player game where they will face
# off with a computer. A player will start with a numer of points. A computer generated number will be a value the player(s)
# have to match. The player(s) bets on themself without betting more than they have. They will pick how many spinners they want,
# the spin value is compared against the target value, whoever is closest wins.>



import random

def printTitleMaterial():
    print("Spinner Winner!")
    print()
    print("By: <Vital Nyabashi>")
    print("[COM S 127 <section 1>]")
    print()


def initialChoice():
    choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    while choice != "p" and choice != "i" and choice != "q":
        print("ERROR: Please enter 'p', 'i', or 'q'...")
        choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    return choice

#
def chooseNumPlayers():
    numPlayers = 0
    while numPlayers != '1' and numPlayers != '2':
        numPlayers = input("How many players? 1 or 2: ")
#       If the user chooses '1,' then they play against the computer
        if numPlayers == '1':
            player1 = 'Human'
            player2 = 'AI'

#       If the user chooses '2,' then they play agianst another human
        else:
            player1 = 'Human1'
            player2 = 'Human2'

        return (player1,player2)


def getSpinnerChoiceHuman(playerNum, target, numSpinners, spinnerLow, spinnerHigh):
    print("Player", playerNum, ", the target value is:", target)
    print("You have", numSpinners, "spinners to choose from.")
    print("Each spinner can generate a value between", spinnerLow, "and", spinnerHigh)
    spinnerChoice = 0
    while spinnerChoice < 1 or spinnerChoice > numSpinners:
        spinnerChoice = int(input("How many spinners would you like to spin? (1-" + str(numSpinners) + "): "))
        if spinnerChoice < 1 or spinnerChoice > numSpinners:
            print("Invalid input. Please choose a number between 1 and", numSpinners)
    print("You have chosen to spin", spinnerChoice, "spinner(s).")
    return spinnerChoice

def wait():
    input("Press [Enter] To Continue...")
    print()


def printBanner():

    print("#######################################################################")
    print()
    print("~~ Starting New Round ~~")
    print()

def printPoints(playerNum, points):
    print("* Player {0} has {1} Points!".format(playerNum, points))
    print()


def wagerPointsHuman(playerNum, points):
    wager = 0
    print("Player", playerNum, "has", points, "points.")
    while wager == 0:
        wager = int(input("How many points would you like to wager? "))
        if wager > int(points):
            print("You can not wager more than you have")
            return wagerPointsHuman(playerNum, points)
        elif wager <= 0:
            print("You can not wager zero or less than zero points")
            return wagerPointsHuman(playerNum, points)
        else:
            print("Player", playerNum, "has wagered", wager, "points.")
            return wager




def wagerPointsAI(playerNum, points):
    wager = 0
    print("Player", playerNum, "has", points, "points.")
    while wager == 0:
        wager = random.randint(1, points+1)
        if wager > points:
            print("You can not wager more than you have")
            return wagerPointsAI(playerNum, points)
        elif wager <= 0:
            print("You can not wager zero or less than zero points")
            return wagerPointsAI(playerNum, points)
        else:
            print("Player", playerNum, "has wagered", wager, "points.")
            return wager


def generateTargetValue(numSpinners, spinnerLow, spinnerHigh):
    num_spinners = random.randint(1, numSpinners + 1)
    spinners = [random.randint(spinnerLow, spinnerHigh) for _ in range(num_spinners)]
    target = sum(spinners)
    print("The target value is:", target)
    return target


def getSpinnerChoiceAI(playerNum, target, numSpinners, spinnerLow, spinnerHigh):
    print("Player", playerNum, ", the target value is:", target)
    print("You have", numSpinners, "spinners to choose from.")
    print("Each spinner can generate a value between", spinnerLow, "and", spinnerHigh)

    spinnerChoice = 0
    while spinnerChoice < 1 or spinnerChoice > numSpinners:
        spinnerChoice = int(input("How many spinners would you like to spin? (1-" + str(numSpinners) + "): "))
        if spinnerChoice < 1 or spinnerChoice > numSpinners:
            print("Invalid input. Please choose a number between 1 and ", numSpinners)

    print("You have chosen to spin", spinnerChoice, "spinner(s).")
    return spinnerChoice


def getSpinnerChoiceAI(playerNum, target, numSpinners, spinnerLow, spinnerHigh):
    print("Player", playerNum, ", the target value is:", target)
    print("You have", numSpinners, "spinners to choose from.")
    print("Each spinner can generate a value between", spinnerLow, "and", spinnerHigh)

    spinnerChoice = 0
    while spinnerChoice < 1 or spinnerChoice > numSpinners:
        spinnerChoice = random.randint(1,numSpinners +1)
        if spinnerChoice < 1 or spinnerChoice > numSpinners:
            print("Invalid input. Please choose a number between 1 and ", numSpinners)

    print("AI have chosen to spin", spinnerChoice, "spinner(s).")
    return spinnerChoice



def spinSpinners(playerNum, spinnerChoice, target, spinnerLow, spinnerHigh):
    print("Player", playerNum, ", the target value is:", target)
    print("Each spinner can generate a value between", spinnerLow, "and", spinnerHigh)

# # TODO: Calculate the total generated by a given number of spinners
# (spinnerChoice)
# # Ex: if spinnerChoice is 3, and you spin 2, 3, and 1, then spinTotal would be 6
    spinTotal = 0
    for i in range(spinnerChoice):
        spinResult = random.randint(spinnerLow, spinnerHigh)
        spinTotal += spinResult
    return spinTotal


def resetGameOptions():
    player1Points = 10
    player2Points = 10
    return player1Points, player2Points


def main():
# # main script running control variable
    running = True
# # gameplay variables
    SPINNER_LOW = 1
    SPINNER_HIGH = 3
    NUM_SPINNERS = 3
    player1Points = 10
    player2Points = 10

# # print the title/ author information
    printTitleMaterial()

# # play the game
    while running:
        choice = initialChoice()
        if choice == "p":
            numPlayers = chooseNumPlayers()
    # # main game loop
            while True:
                printBanner()

                # # Your job is to iteratively build up a game that works - it
                # doesn't really matter how you code it
                # # find a target value
                targetValue = generateTargetValue(NUM_SPINNERS,SPINNER_LOW,SPINNER_HIGH)
                # # player 1 wager
                player1Wager = wagerPointsHuman(numPlayers, wagerPointsHuman)
                # # player 2 wager
                player2Wager = wagerPointsAI(numPlayers, player2Points)
                # # player 1 spin
                player1Spin = getSpinnerChoiceHuman(numPlayers, generateTargetValue,NUM_SPINNERS, SPINNER_LOW,SPINNER_HIGH)
                # # player 2 spin
                player2spin = getSpinnerChoiceAI(numPlayers,generateTargetValue,NUM_SPINNERS,SPINNER_LOW,SPINNER_HIGH)
                # # calculate winner
                if generateTargetValue == player1Points or generateTargetValue == player2Points:
                    print("winner!")
                # # print the points for both players
                    print(player1Points)
                    print(player2Points)
                    print()
                # # check of the game is over - if it is, break out of the gameplay
                # loop and resent the points to default values
                    print("whould you like to play again? If not enter 'q'")
                    x = initialChoice()
                    if x == 'q':
                        print('Thanks for playing! The Game is over')
                # # otherwise print that it is the end of the round



        elif choice == "i":
            print("You will pick pick how many players are playing")
            print("If you pick 1 player, you will face off a computer, if you pick 2 players then you go against another human")
            print("You are assigned 10 from the get go. The goal is to get you pints to as close to the target point.")
            print("First, pick how many spinners you would like to spin at a time")
            print("You will then use a wager to bet on what the next spin number will be ")
            print("The player who gets to the target number will be crowned victor ")
            print()
            pass
        elif choice == "q":
            running = False
            print("Goodbye")
            pass

        else:
            print("ERROR: Variable 'choice' should have been 'p', 'i', or 'q', but instead was: ", choice)
            quit()


if __name__ == "__main__":
    main()


