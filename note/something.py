#!/usr/bin/env python3
""" Docstrings """

import os
import json

def main():
    os.chdir("/home/student/mycode/note/")
    with open("spacex.json", "r") as of:
        space_data = json.load(x)

    print(space_data)
    print(type(space_data))
    print(space_data.get('id'))

main()
