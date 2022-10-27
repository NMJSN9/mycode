#!/usr/bin/python3
# a simple python program to demonstrate getpass.getpass() to read password

import getpass

def main():
    p = getpass.getpass()
    print("password Enter: ", p)

if __name__ =="__main__":
    main()
