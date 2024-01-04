# # "name: Vital Nyabashi"
# # "Creation Date: 2/22/2023"
# # "Lab #: 1"
# # "This will take in a string, your name and reverse it"
#
#

def reverseString(a):
    str = ""
    for i in a:
        str = i + str
    return str

def main():
    name = input("what is your name?: ")
    d = reverseString(name)
    print(d)

if __name__ == "__main__":
    main()

