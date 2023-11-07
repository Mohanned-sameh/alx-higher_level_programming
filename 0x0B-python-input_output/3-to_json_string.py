#!/usr/bin/python3
"""
function: to_json_string
args: my_obj
"""
import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
