#!/usr/bin/python3

"""
function: from_json_string
args: my_str
"""
import json


def from_json_string(my_str):
    """returns an obj represented by a JSON string"""
    return json.loads(my_str)
