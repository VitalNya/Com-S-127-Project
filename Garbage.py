def chooseNumPlayers():
    numPlayers = 0
    s = []
    while numPlayers == 0:
        Num_players = int(input("How many platers are playing?"))
        if Num_players == 1:
            pass
        elif Num_players == 2:
            pass
        else:
            print("Invalid input")
            break
        return Num_players


x = chooseNumPlayers()
print(x)