#!/usr/bin/python3
def uppercase(str):
    for length in range(len(str)):
        char = ord(str[length])
        if char >= 97 and char <= 122:
            char = char - 32
        print("{}".format(chr(char)), end="")
    print()
