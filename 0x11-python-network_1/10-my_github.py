#!/usr/bin/python3
"""Module that takes your Github credentials (username and password) and
uses the Github API to display your id."""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    r = requests.get(
        "https://api.github.com/user",
        auth=HTTPBasicAuth(
            sys.argv[1],
            sys.argv[2],
        ),
    )
    try:
        json = r.json()
        print(json.get("id"))
    except ValueError:
        print("Not a valid JSON")
