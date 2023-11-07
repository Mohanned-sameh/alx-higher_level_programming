#!/usr/bin/python3
"""a function that reads a text file (UTF8) and prints it out to stdout"""


def read_file(filename=""):
    """reads a text file"""
    if filename == "":
        return
    else:
        with open(filename, "r") as f:
            print(f.read(), end="")
