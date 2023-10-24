#!/usr/bin/python3
"""
    Square class instance
"""


class Square:
    """
    A class Square that defines a square by: (based on 3-square.py)
    Args:
    size (int): size of the square
    """

    def __init__(self, size=0):
        self.__size = size

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        self.__size = size
