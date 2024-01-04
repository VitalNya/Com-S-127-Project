# # "name: Vital Nyabashi"
# # "Creation Date: 2/22/2023"
# # "Lab #: 1"
# Ask user for input and return the input into a string
# Then use that string to find the Max or Min


def new_func():
    a = "go"
    s = []
    while a == "go":
        b = str(input("num"))
        if b == "*":
            return s
        s.append(b)


def findMin(c):
    # c = new_func()
    c = [int(i) for i in c]
    print(c)
    min = list[0]
    for number in c:
        if str(number) < str(min):
            min = number
            # print("this is the Min: " + str(min))
    return min


def findMax(c):
    # c = new_func()
    c = [int(i) for i in c]
    print("This is your list: ", c)
    max = c[0]
    for number in c:
        if number > max:
            max = number
        # print("This is the Max: " + str(max))
    return max


def main():
    c = new_func()
    w = findMin(c)
    t = findMax(c)
    print(w)
    print(t)



if __name__ == "__main__":
    main()






