#!/usr/bin/env python3 
""" DOcstring """

import requests

API = "https://api.magicthegathering.io/v1/"

def main():

    resp = requests.get(f"{API}sets")
    print(resp)
main()    
