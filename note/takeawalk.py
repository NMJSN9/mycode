#!/usr/bin/env python3
""" Docstring """

import os

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    
def main():

    lookFor = input("What am I looking for? --> ")
    lookwhere = input("What is the path in which I should search? --> ")

    print(find(lookfor, lookwhere))
main()
