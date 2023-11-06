#!/usr/bin/python3
"""checks if the obj is an instance of specified class"""


def is_same_class(obj, a_class):
    """returns true if obj is an instance of a_class"""
    return type(obj) == a_class
