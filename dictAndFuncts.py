# Vital Nyabashi
# Com s 127
# 4/14/2023


def inputValid():
    var= ''
    for i in range(4):
        while var != ('a'):
            var2 = input("Enter a value for option: 'a','b', 'c', or 'd':" )
            if var2 == 'a' or 'b' or 'c' or 'd':
                var = var + var2
                print(var)
            else:
                pass



print(inputValid())