#!/usr/bin/python3

"""Module that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        json = r.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
