#!/usr/bin/python3
"""This module defines a Rectangle class.
The Rectangle class has two attributes: width and height.
"""


class Rectangle:
    """A class that defines a rectangle.
    Attributes:
        width: The width of the rectangle.
        height: The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle object.
        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle.
        Returns:
            The width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """Retrieves the height of the rectangle.
        Returns:
            The height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.
        Args:
            value: The value to set the width to.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.
        Args:
            value: The value to set the height to.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        for i in range(self.__height):
            for j in range(self.__width):
                result += "#"
            if i < self.__height - 1:
                result += "\n"
        return result

    def __repr__(self):
        """Returns a string representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when a Rectangle object is deleted."""
        print("Bye rectangle...")
