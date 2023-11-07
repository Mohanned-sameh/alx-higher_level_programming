#!/usr/bin/python3
import json

"""
function: load_from_json_file
args: filename
"""


def load_from_json_file(filename):
    """
    load from json file
    """
    with open(filename, "r") as f:
        return json.load(f)
