#!/usr/bin/python3
""" Joseph@TLG learning/ student
    This script is designed to 
    prompt user for birth date 
    and month and identify user's
    zodiac sign with daily horoscope""" 

import time
import sys
from Dict_Zodie import *

## global variables
DAY = ""
MONTH = ""
ZODIAC_SIGN = ""
### Month function ### 

def convert_month():
    """convert number into month"""
    global MONTH      
    #while loop until MONTH = stop
    while   MONTH != "stop":
        #warning telling user when to stop
        print("type stop to exit the application")
        # input as str
        MONTH = input("What is your birth month? (number only): \n")
        #change MONTH into str
        MONTH = int(MONTH)
        # set a var for this function and make sure it's strings
        monthid = MONTH
        # take information from imported dictionary
        insertedinput = months_dictionary2["months"][monthid]
        try:
            if MONTH > 0 and MONTH < 13:
                MONTH = insertedinput
                break
            elif MONTH == "stop": 
                print("Application stopped")
            else:
                print("Invalid input, make sure to only type 1-12!!")
                time.sleep(2)
        except KeyError:
            print("invalid input, please enter only numeric input")
            time.sleep(2)

def input_day():
    """Identify the max var int value from dictionary"""
    global MONTH
    global DAY
    
    # set a var for this function and make sure it's strings
    monthid = str(MONTH)
    #itake information from improted dictionary
    insertedinput = months_dictionary["months"][monthid]
    insertedinput = int(insertedinput)
    
    # looping until DAY = "stop" 
    while DAY != "stop":
        # input as
        DAY = input("What is your birth day? (number only): \n")
        print("type 'stop' to stop") 
        # convert DAY var to  an interger
       
       #DAYy = int(DAY)
        try:
            if int(DAY) <= 0:
                print(f"invalid input, please enter only 1-{insertedinput}")
                time.sleep(2)
            elif int(DAY) > insertedinput:
                print(f"invalid input, please enter only 1-{insertedinput}")
                time.sleep(2)
            elif int(DAY) >= 1:
                print("date accepted")
                break
            elif int(DAY) <= insertedinput:
                print("date accepted")
                break
            else:
                print("invalid input, please enter only numeric input")
                time.sleep(2)
        # if user input anything other than integer it will continue to loop
        except ValueError:
            print("invalid input, please enter only numeric input")
            time.sleep(2)
            continue

def id_zodiac():
    """Identify user Zodiac sign"""
    global ZODIAC_SIGN
    global MONTH

    # set variable inside the function
    yourmonth = MONTH
    yourday = int(DAY)
    # set a var for this function and make sure it's strings
    monthid = str(MONTH)
    # take information from improted dictionary
    maxoutput = zodiacsplit_dictionary["months"][monthid]
    maxoutput = int(maxoutput)
    
    if yourmonth == MONTH:
        # if statement to define user's date
        if yourday > 0 and yourday < maxoutput:
            i = 0
        else:
            i = 1
            ZODIAC_SIGN = "Aquarius"
        # set a var for this function and make sure it's strings
        narrow_id = str(MONTH)+str(i)
        ZODIAC_SIGN = zodiac_dictionary["zsign"][narrow_id]
        print("Your Zodiac sign is " + ZODIAC_SIGN)
    else:
        print("Error")
        time.sleep(3)
        print("Please restart the application")
        sys.exit()

def read_horoscope():
    """Read user horoscope from a file, supposedly updated daily, could use api"""
    global ZODIAC_SIGN
    print(ZODIAC_SIGN)
    with open(f"{ZODIAC_SIGN}.txt", "r") as readfile:
        readfile = readfile.read()
        print(readfile)

def main():
    """Read user horoscope from a file, supposedly updated daily, could use api"""
    global MONTH
    global DAY
    
    # excecute prompt the month input
    convert_month()
    # excecute prompt the day
    input_day()
    
    # if user chose to quit by typing stop
    if DAY == 'stop':
        print("Goodbye")
        sys.exit()
    else:
        # change into str
        DAY = str(DAY)
        print("your birthday is " + DAY + " in "+ MONTH)
        #print("your birthday is " + yourday + " in ")
    
    # execute identify user zodiac sign
    id_zodiac()
    # asking if user wants to read their daily horoscope
    read_yoursign = input("Would you like to read your daily horoscope? (Y/N): \n")
    
    if read_yoursign.lower() == "y":
        print("")
        read_horoscope()
    elif read_yoursign.lower() == "n":
        print("application closed")
    # if user type anything other that "y" and "n" will print different statement
    else:
        print("invalid response, application closed")

if __name__ == "__main__":
    main()
