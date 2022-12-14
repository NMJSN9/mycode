#!/usr/bin/python3
""" This is dictionary file script 
    Author: Joseph Nine """
import json

months_dictionary = { 
        "months_dictionary" :
            {
                "January": 31,
                "February": 29,
                "March": 31,
                "April": 30,
                "May": 31,
                "June": 30,
                "July": 31,
                "August": 31,
                "September": 30,
                "October": 31,
                "November": 30,
                "December": 31
            }
}
months_dictionary2 = { 
        "months_dictionary2" :
            {
                1: "January",
                2: "February",
                3: "March",
                4: "April",
                5: "May",
                6: "June",
                7: "July",
                8: "August",
                9: "September",
                10: "October",
                11: "November",
                12: "December"
            }
}
zodiacsplit_dictionary = { 
        "zodiacsplit_dictionary" :
            {
                "January": 20,
                "February": 19,
                "March": 21,
                "April": 20,
                "May": 21,
                "June": 21,
                "July": 23,
                "August": 23,
                "September": 23,
                "October": 23,
                "November": 22,
                "December": 22
            }
}
zodiac_dictionary = { 
        "zodiac_dictionary" :
            {
                "January0": "Capricorn",
                "January1": "Aquarius",
                "February0": "Aquarius",
                "February1": "Pisces",
                "March0": "Pisces",
                "March1": "Aries",
                "April0": "Aries",
                "April1": "Taurus",
                "May0": "Taurus",
                "May1": "Gemini",
                "June0": "Gemini",
                "June1": "Cancer",
                "July0": "Cancer",
                "July1": "Leo",
                "August0": "Leo",
                "August1": "Virgo",
                "September0": "Virgo",
                "September1": "Libra",
                "October0": "Libra",
                "October1": "Scorpio",
                "November0": "Scorpio",
                "November1": "Sagittarius",
                "December0": "Sagittarius",
                "December1": "Capricorn"

                
            }
}





with open("zodie_dict.json", "w") as outfile:
	json.dump(months_dictionary, outfile)
	json.dump(months_dictionary2, outfile)
	json.dump(zodiacsplit_dictionary, outfile)
	json.dump(zodiac_dictionary, outfile)
