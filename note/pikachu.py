#!/usr/bin/python3 
""" Docstring """

import requests

def main():
    pokenum = input("Pick a number between 1 and 151!\n> ")
    pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()
    
    print(type(pokeapi))
    print(pokeapi)

main()

