#!/usr/bin/python3
"""
function: class_to_json
args: filename
"""
import json


def class_to_json(filename):
    """returns a dict description with simple data struct"""
    with open(filename, "r") as f:
        return json.load(f)
