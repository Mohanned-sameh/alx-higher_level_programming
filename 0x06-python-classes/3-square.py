#!/usr/bin/python3
"""
Square class
"""


class Square:
    """
    declares a square class
    args:
        size: size of the square

    """

    def __init__(self, size=0):
        self.size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size

    def area(self):
        """
        returns the area of the square
        """
        return self.size * self.size
