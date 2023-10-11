#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key].append(value)
    elif 2 * key in a_dictionary:
        a_dictionary[2 * key].append(value)
    else:
        a_dictionary[2 * key] = [value]
    return a_dictionary
