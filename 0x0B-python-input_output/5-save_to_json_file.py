#!/usr/bin/python3
"""
function: save_to_json
args: my_obj, filename
"""
import json


def save_to_json(my_obj, filename):
    """writes an obj to a text file using JSOn"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
