#!/usr/bin/python3
import json
import os

os.chdir("/home/student/project/")


with open('zodie_dict.json', 'r') as of:
    something = json.load(of)

   
print(type(something))
print(f"{something}")
    #openfile = json.load(openfile)
    #print(openfile)


