#!/usr/bin/python3
"""
class: student
public instance: first_name, last_name, age
"""


class Student:
    """init with self, first_name, last_name, age"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """Public method: to_json(self)
    that retrieves a dictionary representation of a Student instance
    """

    def to_json(self):
        return self.__dict__
