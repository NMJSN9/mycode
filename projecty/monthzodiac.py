#!/usr/bin/python3
""" Month """

        
      # input as str
mont = "default"        
#while loop until mont = stop
while   mont != "stop":
            # input as str
        mont = input("What is your birth month? (number only): \n")
                    #change mont into str
        mont = str(mont)

        print("type stop to exit the application")
        if mont == "1" :
            print("January")
        elif mont == "2":
            print("Febuary")
        elif mont == "3":
            print("March")
        elif mont == "4":
            print("April")
        elif mont == "5":
            print("May")
        elif mont == "6":
            print("June")
        elif mont == "7":
            print("July")
        elif mont == "8":
            print("August")
        elif mont == "9":
            print("Septempber")
        elif mont == "10": 
            print("October")
        elif mont == "11": 
            print("November")
        elif mont == "12": 
            print("December")
        elif mont == "stop": 
            print("Application stopped")
        else:
            print("Invalid input, make sure to only type 1-12!!")
