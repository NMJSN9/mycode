#!/usr/bin/python3
""" day """


# input as
dae = input("What is your birth day? (number only): \n")
#change mont into str
dae = int(dae)

def datecal():


    if dae <= 0:
        print("invalid input, please enter only 1-31")
    elif dae >= 32:
        print("invalid input, please enter only 1-31")
    elif dae >= 1:
        print(f"date accepted")
    elif dae <= 31:
        print(f"date accepted")
    else:
        print("invalid input, please enter only numeric input")
datecal()

