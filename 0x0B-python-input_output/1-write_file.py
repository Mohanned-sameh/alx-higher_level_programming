#!/usr/bin/python3
"""
function: write_file
args: filename , text
"""


def write_file(filename="", text=""):
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
