#!/usr/bin/python3
""" Docstring """

import requests



NASAAPI = "https://api.nasa.gov/planetary/apod?"

def returncreds():
    with open("/home/student/mycode/note/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()

        nasacreds = "api_key=" + nasacreds.strip("\n")
        return nasacreds
# url.com/endpoint?api_key=jfklreksef&date=YYYY-MM_DD
def main():
    nasacreds = returncreds()
    date = input("You knowwhat to do: ) 
    apodresp = erquests.get(NASAAPI + nasacreds)
    apod = apodresp.json()

    print(apod)

if __name__ == "__main__":
    main()
