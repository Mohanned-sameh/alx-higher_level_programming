#!/usr/bin/python3
"""
checks if the object is an instance of a class (direclty or indirectly)
from the specified class
"""


def inherits_from(obj, a_class):
    """
    checks if the object is an instance of a class (direclty or indirectly)
    from the specified class
    """
    return issubclass(isinstance(obj, a_class) and type(obj) != a_class)
