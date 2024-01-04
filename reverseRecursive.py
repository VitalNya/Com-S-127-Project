# Vital Nyabashi      4/27/2023
# Com s 127: Lab 16 reverseRecursive.py


def reverseRecursive(string):
    # Base case
    if len(string) == 1:
        return string
    # Recursive case
    else:
        return reverseRecursive(string[1:]) + string[0]


def main():
    user_input = input("Enter a string to reverse: ")
    reversed_string = reverseRecursive(user_input)
    print("Reversed string:", reversed_string)


if __name__ == "__main__":
    main()