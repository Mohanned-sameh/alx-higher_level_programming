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

    @property
    def size(self):
        """
        returns the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
            return self.__size

    def my_print(self):
        """
        prints the square
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
            return
        return
