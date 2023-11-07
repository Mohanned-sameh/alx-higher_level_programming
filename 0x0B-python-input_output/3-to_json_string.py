#!/usr/bin/python3


import json

"""
function: to_json_string
returns: json representation of an object
"""


def to_json_string(my_obj):
    """function to represent json of an object"""
    if my_obj is None:
        return None
    else:
        return json.dumps(my_obj)
