#!/usr/bin/python3

"""
Function: load_from_json_file
args: filename
"""
import json


def load_from_json_file(filename):
    """creates an object from a JSON file"""
    with open(filename, "r") as f:
        return json.load(f)
