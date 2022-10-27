#!/usr/bin/python3
""" Joseph@TLG learning/ student""" 
#import dayzodiac
#import monthzodiacedit
#from monthZodiac import *
#import dayzodiac


dae = ""
mont = ""

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


                                    ### Month function ### 


        
def monthZodie():
    
    global mont      
              # input as str
    #while loop until mont = stop
    while   mont != "stop":
            #warning telling user when to stop
            print("type stop to exit the application")
            # input as str
            mont = input("What is your birth month? (number only): \n")
                        #change mont into str
            mont = str(mont)
            
            
            ## start if statment
            if mont == "1" :
                mont = "January" 
                break
            elif mont == "2":
                mont = "Febuary"
                break
            elif mont == "3":
                mont = "March"
                break
            elif mont == "4":
                mont = "April"
                break
            elif mont == "5": 
                mont = "May"
                break
            elif mont == "6":
                mont = "June"
                break
            elif mont == "7":
                mont = "July"
                break
            elif mont == "8":
                mont = "August"
                break
            elif mont == "9":
                mont = "September"
                break
            elif mont == "10": 
                mont = "October"
                break
            elif mont == "11": 
                mont = "November"
                break
            elif mont == "12": 
                mont = "December"
                break
            elif mont == "stop": 
                print("Application stopped")
            else:
                print("Invalid input, make sure to only type 1-12!!")




####


"""{month_dict = {
                {31 : ['January', 'March', 'May', 'July', 
                'August', 'October', 'December']},
                {30 : ['September','April','June', 'November']},
                {29 : 'Febuary'}
                }
print(month_dict.dir()) 
#error"""



def dayZodie():
    global mont
    global dae

    while dae != "stop":
        # input as
        dae = input("What is your birth day? (number only): \n")
        print("type 'stop' to stop")
        #change mont into str
        dae = int(dae)
        #while month_dict ==
        if dae <= 0:
            print("invalid input, please enter only 1-31")
        elif dae >= 32:
            print("invalid input, please enter only 1-31")
        elif dae >= 1:
            print(f"date accepted")
            break
        elif dae <= 31:
            print(f"date accepted")
            break
        else:
            print("invalid input, please enter only numeric input")



def main():
    global mont
    global dae

    monthZodie()
    dayZodie()
    yourmonth = mont
    yourday = dae
   
    # change into str
    yourday = str(yourday)
    print("your birthday is " + yourday + " in "+ yourmonth)
    #print("your birthday is " + yourday + " in ")

if __name__ == "__main__":
    main()
