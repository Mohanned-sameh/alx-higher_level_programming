#!/usr/bin/python3
"""
This module adds all arguments to a Python list and then save them to a file
"""
import sys
from os import path

save_module = __import__("save_to_json_file")
load_module = __import__("load_from_json_file")

file_name = "add_item.json"
data = []
if path.exists(file_name):
    data = load_module.load_from_json_file(file_name)

data += sys.argv[1:]

save_module.save_to_json_file(data, file_name)
