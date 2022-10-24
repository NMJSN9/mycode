#!/usr/bin/python3
""" EXPLORE READ """
"""
## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

## display file to the screen - .read()
print(configfile.read())


configlist = configfile.readlines()
print(configlist)
#print(type(configlist))

configfile.seek(0, 0) # reset to the top of the file to continue doing what 
## Iterate through configlist
for x in configlist:
    print(x)

configfile.close() # always close your file
"""
######## EXPLORE READ ##########
## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

## display file to the screen - .read()
#print(configfile.read())

## close file
configfile.close()

######## EXPLORE READLINES ##########
## re-create file object to explore new method
configfile = open("vlanconfig.cfg", "r")

## make a list of file lines - .readlines()
configlist = configfile.splitlines()
print(configlist)

## Iterate through configlist
for x in configlist:
    x = x.strip()
    print(x, end=" ")

## Always close your file
configfile.close()

