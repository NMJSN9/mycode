#!/usr/bin/python3
""" Joseph@TLG learning/ student""" 
#import dayzodiac
#import monthzodiacedit
from monthZodiac import *
import dayzodiac


# change into str
yourday = str(dayzodiac.dae)
yourmonth = str(mont)


print("your birthday is " + yourday + " in "+ yourmonth)
yourday = int(yourday)


def idZodie():
    #January    
    if yourmonth == "January":
        if yourday > 0 and yourday < 20:
            #if youday <= 19:
            zsign = "Capricorn"
            print("Your Zodiac sign is " + zsign)
        else:
            zsign = "Aquarius"
            print("Your Zodiac sign is " + zsign)
            
    # Febuary condition
    elif yourmonth == "Febuary":
        if yourday > 0 and yourday < 19:
            #if youday <= 19:
            zsign = "Aquarius"
            print("Your Zodiac sign is " + zsign)
        else:
            zsign = "Pisces"
            print("Your Zodiac sign is " + zsign)
    #March condition        
    elif yourmonth == "March":
        if yourday > 0 and yourday < 21:
            zsign = "Pisces"
            print("Your Zodiac sign is " + zsign)
        else:
            zsign = "Aries"
            print("Your Zodiac sign is " + zsign)
    # April condition
    elif yourmonth == "April":
        if yourday > 0 and yourday < 20 :
            zsign = "Aries"
            print("Your Zodiac sign is " + zsign)
        else:
            zsign = "Taurus"
            print("Your Zodiac sign is " + zsign)
    # May condition
    elif yourmonth == "May":
        if yourday > 0 and yourday < 21:
            
            zsign = "Taurus"
            print("Your Zodiac sign is " + zsign)
        else:
            zsign = "Gemini"
            print("Your Zodiac sign is " + zsign)
    # June
    elif yourmonth == "June":
        if yourday > 0 and yourday < 21:
            
            zsign = "Gemini"
            print("Your Zodiac sign is " + zsign)
        else:
            zsign = "Cancer"
            print("Your Zodiac sign is " + zsign)
    # July
    elif yourmonth == "July":
        if yourday > 0 and yourday < 23:
            
            zsign = "Cancer"
            print("Your Zodiac sign is " + zsign)
        else:
            zsign = "Leo"
            print("Your Zodiac sign is " + zsign)
    # August
    elif yourmonth == "August":
        if yourday > 0 and yourday < 23:
            
            zsign = "Leo"
            print("Your Zodiac sign is " + zsign)
        else:
            zsign = "Virgo"
            print("Your Zodiac sign is " + zsign)
    # September
    elif yourmonth == "September":
        if yourday > 0 and yourday < 23:
            
            zsign = "Virgo"
            print("Your Zodiac sign is " + zsign)
        else:
            zsign = "Libra"
            print("Your Zodiac sign is " + zsign)
    # October
    elif yourmonth == "October":
        if yourday > 0 and yourday < 23:
            
            zsign = "Libra"
            print("Your Zodiac sign is " + zsign)
        else:
            zsign = "Scorpio"
            print("Your Zodiac sign is " + zsign)
    # November
    elif yourmonth == "November":
        if yourday > 0 and yourday < 22:
            
            zsign = "Scorpio"
            print("Your Zodiac sign is " + zsign)
        else:
            zsign = "Sagittarius"
            print("Your Zodiac sign is " + zsign)
    # December
    elif yourmonth == "December":
        if yourday > 0 and yourday < 22:
            
            zsign = "Sagittarius"
            print("Your Zodiac sign is " + zsign)
        else:
            zsign = "Capricorn"
            print("Your Zodiac sign is " + zsign)
    else:
        print("Error")
idZodie()
"""
def main():
    idZodie()
main()
"""
