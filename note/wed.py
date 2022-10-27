#!/usr/bin/python3
""" DOcstring"""

import requests 

MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    """ runtim code """

    groundctrl = requests.get(MAJORTOM)
    helmetson = groundctrl.json()

    print("\n\nConverted Python Data")
    print(helmetson)

main()
