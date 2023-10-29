#!/usr/bin/python3

"""
function: print_square
parameters: size

"""


def print_square(size):
    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")
    if type(size) is int and size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    size = int(size)
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
