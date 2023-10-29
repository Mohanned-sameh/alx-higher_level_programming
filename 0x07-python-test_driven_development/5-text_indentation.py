#!/usr/bin/python3

"""
function: text_indentation
args: text
 prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if i in ".?:":
            print(i)
            print()
        else:
            print(i, end="")
