# Vital Nyabashi
# Com s 127 Lab Week 10
# Our task is to use/ create/ modify files. We will take in studentData.text
# and do what we wish to it.

# lets call the file

def main():
    file = open("studentData.text","r") # We have grabbed the file
    threshold = int(input("what would you like the threshold to be: ")) # The threshold is not defined yet so i just set it as this value. It can be changed if needed
    print("What is you threshold value?: " + str(threshold)) # Print out what your threshold is
    print()

    # We want to go in the file of lists and section them
    for i in file:
        values = i.split()
        numbers = values[1:]
        names = values[0]
        greater_than = 0
        less_than = 0
        int_numbs = list(map(int, numbers)) # turning the list of str. numbers into list of int.
        # print(int_numbs)

        for i in int_numbs:
            if int(i) >= threshold:
                greater_than += 1
            else:
                less_than += 1
        print(names + ': ' + str(greater_than) + " score >= " + str(threshold) + ', ' + str(less_than) + " scores < " + str(threshold))


if __name__ == "__main__":
    main()

