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

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict

    """Public method: reload_from_json(self, json)
    that replaces all attributes of the Student instance
    """

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
