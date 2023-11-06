#!/usr/bin/python3
"""
checks if a obj is of instance or is an instance 
of a class that inherits from the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    checks if a obj is of instance or is an instance
    of a class that inherits from the specified class
    """
    return isinstance(obj, a_class)
