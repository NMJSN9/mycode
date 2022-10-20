#!/usr/bin/python3
""" Month """

        
      # input as str
mont = "default"        
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
            mont = "Septempber"
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




