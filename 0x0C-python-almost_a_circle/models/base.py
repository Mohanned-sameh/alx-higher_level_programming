#!/usr/bin/python3
"""Class: Base
private class attribute: __no_objects = 0
class constructor: def __init__(self, id=None):
"""


class Base:
    """
    private class __no_objects
    public class constructor: def __init__(self, id=None)
    """

    __no_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__no_objects += 1
            self.id = Base.__no_objects
