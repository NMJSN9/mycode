#!/usr/bin/python3
"""DOCSTRIGNS"""

import netifaces


#print(type(netifaces.interfaces()))
netread = netifaces.interfaces()

for i in netread:
    print('\m*********Detals of Interfaces()' + i + ' **********')
    try:
        print('MAC: ', end='')
        print((netifaces.ifaddresses9i)[netifaces.AF_:
