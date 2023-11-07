#!/usr/bin/python3

import json

"""
function: to_json_string
args: my_obj
returns: JSON representation of my_obj
"""


def to_json_string(my_obj):
    """JSON representaition of my_obj"""
    return json.dumps(my_obj)
