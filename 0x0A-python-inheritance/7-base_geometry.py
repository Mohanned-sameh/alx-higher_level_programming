#!/usr/bin/python3
"""
class: BaseGeometry
public instance method: def area(self): that raises an exception
public instance method: def integer_validator(self, name, value): that
validates value
"""


class BaseGeometry:
    """
    class BaseGeometry
    """

    def area(self):
        """
        raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value
