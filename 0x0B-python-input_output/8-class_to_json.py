#!/usr/bin/python3
"""
function: class_to_json
args: filename
"""


def class_to_json(filename):
    """
    returns a dict description with simple data struct
    """
    return vars(filename)
