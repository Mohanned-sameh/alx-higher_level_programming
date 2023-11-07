#!/usr/bin/python3
"""
function: write_file
args: filename , text
"""


def write_file(filename="", text=""):
    """writes specified text within a specified file"""
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
