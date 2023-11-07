#!/usr/bin/python3
import json

"""
function: from_json_string
args: my_str
"""


def from_json_string(my_str):
    """returns an obj represented by a JSON string"""
    return json.loads(my_str)
