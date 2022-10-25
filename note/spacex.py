#!/usr/bin/env pythone3
""" DOCSTRING """

import os
import requests

API = "https://api.spacexdata.com/v3/dragons/dragon1"

def main():
    """ runtime code"""

    os.chdir("/home/student/examples")
    response = requests.get(API)

    space_data = response.json()

    print(space_data)
    print()

