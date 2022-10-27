#!/usr/bin/python3
"""tracking the iss using
   api.open-notify.org/astros.json | Alta3 Research"""

# notice we no longer need to import urllib.request or json
import requests
import datetime

## Define URL
ISS_TRACK= 'http://api.open-notify.org/iss-now.json'

def main():
    """runtime code"""

    ## Call the webservice
    requestIss = requests.get(ISS_TRACK)

    ## translate the json into python lists and dictionaries
    jsonIssTrack = requestIss.json()
    #print(jsonIssTrack['timestamp'] + j)
    Therealdatetime = datetime.datetime.fromtimestamp(jsonIssTrack['timestamp'])
    print(f"CURRENT LOCATION OF THE ISS: \nTimestamp: {Therealdatetime}\nLon: {jsonIssTrack['iss_position']['longitude']} \nLat: {jsonIssTrack['iss_position']['latitude']}")
    
    #print('\n\nPeople in Space: ', helmetson['number'])
    #people = helmetson['people']
    #print(people)
    #for i in people:
       # print(i['name']+ " on the " + i['craft'])
if __name__ == "__main__":
    main()

