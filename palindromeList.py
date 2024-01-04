# Vital Nyabshi     Section 1
# Lab 7 assignment
# Takin in a string list from user and check if it is a palindrome

print('Com s 127')
print('Vital Nyabashi')
print('lab 7 Assignment: palindromeList')
print('Date complete: 3/01/2023')
print()

def new_func():
    a = "go"
    s = []
    while a == "go":
        b = str(input("Word"))
        if b == "*":
            return s
        s.append(b)


def palindromeList():
    lista = new_func()
    is_palindrome = True
    for i in range(len(lista)):
        if lista[i] != lista[len(lista) - i - 1]:
            is_palindrome = False
    return is_palindrome
    # if is_palindrome:
    #     # print("This is a palindrome"+ (str(lista)))
    #     return True
    # else:
    #     print("This is not a palindrome" + (str(lista)))
    #     return is_palindrome


def main():
    d = palindromeList()
    print(d)


if __name__ == "__main__":
    main()

