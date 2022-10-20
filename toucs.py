#!/usr/bin/python3
""" Fun with If"""

hostname = input("What value shoudl we set for hostname? --> ")

if hostname.lower() == "mtg":
    print("The hostname was found to be mtg.")
    print("hostname matches the expected configuration.")
elif hostname.lower() == "bear":
    print("We have a strict no bears policy!")
else:
    print("You're super scary. I don't like you.")
    print("hostname does not match the expected configuration.")

print("Exiting the script")

