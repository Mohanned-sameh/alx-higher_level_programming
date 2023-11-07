#!/usr/bin/python3
"""
function: write_file
args: filename , text
"""


def write_file(filename="", text=""):
    """writes in a specific file a given text"""
    if filename == "" or text == "":
        return False
    else:
        with open(filename, "w") as f:
            f.write(text)
