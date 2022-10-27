#!/usr/bin/python3
"""Docstrings """

import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n*****************Details of INterfaces - ' + i + ' ****************')
    try: # this is a new line, younalso need to indent the code below
        print('MAC: ', end='') # this print statement will always print MAC without an end of lin
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) # print Mac   
        print('IP: ', end='') # this print statement will always print MAC without an end of lin
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']) # print IP
    except:
        print('Could not collect adapter information') # Print an error mesg
