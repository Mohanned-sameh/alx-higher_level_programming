#!/usr/bin/python3
"""
This module adds all arguments to a Python list and then save them to a file
"""
import os.path
import sys


def main():
    filename = "add_item.json"
    json_list = []

    try:
        save = __import__("5-save_to_json_file").save_to_json_file
        load = __import__("6-load_from_json_file").load_from_json_file

        if os.path.exists(filename):
            json_list = load(filename)

        json_list.extend(sys.argv[1:])

        save(json_list, filename)
    except ImportError:
        print("Error: Unable to import the necessary modules.")


if __name__ == "__main__":
    main()
