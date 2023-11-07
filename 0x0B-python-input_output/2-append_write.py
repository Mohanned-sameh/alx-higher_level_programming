#!/usr/bin/python3
"""
function: append_write
args: filename, text
appends text at the end of a file
"""


def append_write(filename="", text=""):
    """append specified text in a specified file at the end of it"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
