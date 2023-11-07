#!/usr/bin/python3
"""
a script that adds all arguments to a python list and then save them to a file.
"""

from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    save_to_json_file(args, "list.json")
    print(load_from_json_file("list.json"))
