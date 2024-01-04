
# palindromeCheck.py

# # name: Vital Nyabashi
# # Creation Date: 2/22/2023
# # Lab #: 1
# #

import reverseString

def palindromeCheck(d):
    reversed_word = reverseString.reverseString(d)
    if reversed_word == d:
        print("Yes this is a palindrome: " + d)
    else:
        print("This is not a palindrome: " + d)


def main():
    word = input("Write a palindrome: ")
    palindromeCheck(word)

if __name__ == "__main__":
    main()


